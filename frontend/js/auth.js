const passwordToggles = document.querySelectorAll("[data-toggle-password]");
const accountsStorageKey = "obrae.demo.accounts";
const shopAccountsStorageKey = "obrae.demo.shop-accounts";
const passwordHashIterations = 150000;

passwordToggles.forEach((toggle) => {
  toggle.addEventListener("click", () => {
    const field = document.getElementById(toggle.dataset.togglePassword);
    const isVisible = field.type === "text";

    field.type = isVisible ? "password" : "text";
    toggle.setAttribute("aria-pressed", String(!isVisible));
    toggle.setAttribute("aria-label", isVisible ? "Mostrar senha" : "Ocultar senha");
  });
});

function showFormMessage(form, message, isSuccess) {
  const status = document.getElementById(`${form.id.replace("-form", "")}-message`);

  status.textContent = message;
  status.classList.toggle("success", isSuccess);
}

function validateForm(form) {
  if (!form.reportValidity()) {
    return false;
  }

  if (form.id === "register-form" || form.id === "shop-register-form") {
    const password = form.elements.senha;
    const confirmation = form.elements.confirmar_senha;

    if (password.value !== confirmation.value) {
      confirmation.setCustomValidity("As senhas não correspondem.");
      confirmation.reportValidity();
      confirmation.setCustomValidity("");
      return false;
    }
  }

  return true;
}

function getAccounts(storageKey) {
  const savedAccounts = localStorage.getItem(storageKey);

  if (savedAccounts === null) {
    return [];
  }

  const accounts = JSON.parse(savedAccounts);
  if (!Array.isArray(accounts)) {
    throw new Error("Os dados de demonstração salvos no navegador são inválidos.");
  }

  return accounts;
}

function bytesToHex(bytes) {
  return Array.from(bytes, (byte) => byte.toString(16).padStart(2, "0")).join("");
}

function hexToBytes(hex) {
  if (!/^(?:[0-9a-f]{2})+$/i.test(hex)) {
    throw new Error("O cadastro salvo no navegador contém uma senha inválida.");
  }

  return new Uint8Array(hex.match(/.{2}/g).map((byte) => parseInt(byte, 16)));
}

async function hashPassword(password, salt) {
  if (!window.crypto || !window.crypto.subtle) {
    throw new Error("Este navegador não oferece suporte à validação local de senha.");
  }

  const passwordKey = await window.crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(password),
    "PBKDF2",
    false,
    ["deriveBits"]
  );
  const hash = await window.crypto.subtle.deriveBits(
    {
      name: "PBKDF2",
      salt,
      iterations: passwordHashIterations,
      hash: "SHA-256",
    },
    passwordKey,
    256
  );

  return bytesToHex(new Uint8Array(hash));
}

async function registerAccount(form) {
  const email = form.elements.email.value.trim().toLowerCase();
  const isShop = form.id === "shop-register-form";
  const storageKey = isShop ? shopAccountsStorageKey : accountsStorageKey;
  const accounts = getAccounts(storageKey);

  if (accounts.some((account) => account.email === email)) {
    showFormMessage(form, "Já existe uma conta de demonstração com este e-mail.", false);
    return;
  }

  const shopDetails = isShop
    ? {
        street: form.elements.rua.value.trim(),
        streetNumber: form.elements.numero_endereco.value.trim(),
        postalCode: form.elements.cep.value.replace(/\D/g, ""),
        cnpj: form.elements.cnpj.value.replace(/\D/g, ""),
        city: form.elements.cidade.value.trim(),
        state: form.elements.estado.value.trim().toUpperCase(),
      }
    : {};

  if (isShop && accounts.some((account) => account.cnpj === shopDetails.cnpj)) {
    showFormMessage(form, "Já existe uma conta de demonstração com este CNPJ.", false);
    return;
  }

  const salt = window.crypto.getRandomValues(new Uint8Array(16));
  const saltHex = bytesToHex(salt);
  const passwordHash = await hashPassword(form.elements.senha.value, salt);

  accounts.push({
    name: isShop ? form.elements.nome_loja.value.trim() : form.elements.nome.value.trim(),
    email,
    phone: form.elements.telefone.value.trim(),
    ...shopDetails,
    salt: saltHex,
    passwordHash,
  });
  localStorage.setItem(storageKey, JSON.stringify(accounts));
  window.location.assign(isShop ? "admin.html" : "index.html");
}

async function loginAccount(form) {
  const email = form.elements.email.value.trim().toLowerCase();
  const password = form.elements.senha.value;
  const isShop = form.id === "shop-login-form";
  const storageKey = isShop ? shopAccountsStorageKey : accountsStorageKey;
  const account = getAccounts(storageKey).find((savedAccount) => savedAccount.email === email);

  if (!account) {
    showFormMessage(form, "E-mail ou senha inválidos.", false);
    return;
  }

  const salt = hexToBytes(account.salt);
  const passwordHash = await hashPassword(password, salt);

  if (passwordHash !== account.passwordHash) {
    showFormMessage(form, "E-mail ou senha inválidos.", false);
    return;
  }

  window.location.assign(isShop ? "admin.html" : "index.html");
}

document.querySelectorAll("[data-auth-submit]").forEach((button) => {
  const form = document.getElementById(button.dataset.authSubmit);

  const handleAttempt = async () => {
    const status = document.getElementById(`${form.id.replace("-form", "")}-message`);
    status.textContent = "";
    status.classList.remove("success");

    if (!validateForm(form)) {
      return;
    }

    try {
      if (form.id === "register-form" || form.id === "shop-register-form") {
        await registerAccount(form);
      } else {
        await loginAccount(form);
      }
    } catch (error) {
      console.error("Não foi possível concluir a autenticação de demonstração.", error);
      showFormMessage(
        form,
        "Não foi possível concluir. Verifique o armazenamento local do navegador e tente novamente.",
        false
      );
    }
  };

  button.addEventListener("click", handleAttempt);
  form.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && event.target.tagName !== "BUTTON") {
      event.preventDefault();
      handleAttempt();
    }
  });
});
