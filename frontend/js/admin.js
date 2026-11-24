/* ==========================================================================
   DADOS SIMULADOS (MOCK DATA) PARA CADA ABA
   O backend futuramente fornecerá esses dados via API.
   ========================================================================== */

// 1. Dados da aba "Estoque"
const dadosEstoque = [
  { id: "#EST-101", nome: "Cimento Votoran 50kg", categoria: "Materiais", qtd: 150, preco: 32.90, status: "Em Estoque" },
  { id: "#EST-102", nome: "Tinta Acrílica Suvinil 18L", categoria: "Pintura", qtd: 24, preco: 329.90, status: "Estoque Baixo" },
  { id: "#EST-103", nome: "Furadeira DeWalt 650W", categoria: "Ferramentas", qtd: 12, preco: 279.90, status: "Em Estoque" },
  { id: "#EST-104", nome: "Torneira Docol Cozinha", categoria: "Hidráulica", qtd: 35, preco: 119.90, status: "Em Estoque" }
];

// 2. Dados da aba "Pedidos" (Formato detalhado que você aprovou)
const dadosPedidos = [
  {
    id: "#9482",
    cliente: "Carlos Eduardo Silva",
    data: "11/11/2026 - 14:30",
    itens: "Cimento Votoran 50kg (x5), Furadeira DeWalt 650W (x1)",
    total: 444.40,
    status: "Pendente"
  },
  {
    id: "#9481",
    cliente: "Mariana Souza",
    data: "11/11/2026 - 11:15",
    itens: "Tinta Acrílica Suvinil 18L (x1)",
    total: 329.90,
    status: "Em Separação"
  },
  {
    id: "#9480",
    cliente: "Roberto Alves",
    data: "10/11/2026 - 18:40",
    itens: "Torneira para cozinha Docol (x2)",
    total: 239.80,
    status: "Entregue"
  },
  {
    id: "#9479",
    cliente: "Fernanda Lima",
    data: "10/11/2026 - 09:20",
    itens: "Cimento Votoran 50kg (x10)",
    total: 329.00,
    status: "Entregue"
  }
];

// 3. Dados da aba "Materiais" (Catálogo de produtos cadastrados)
const dadosMateriais = [
  { id: "#MAT-01", nome: "Cimento Votoran CP II-F-32", tipo: "Saco 50kg", precoUnit: 32.90, fornecedor: "Votorantim" },
  { id: "#MAT-02", nome: "Areia Média Lavada", tipo: "Metro cúbico (m³)", precoUnit: 89.00, fornecedor: "Pedreira Local" },
  { id: "#MAT-03", nome: "Tijolo Baiano 8 furos", tipo: "Milheiro", precoUnit: 750.00, fornecedor: "Cerâmica Santa Rita" },
  { id: "#MAT-04", nome: "Brita nº 1", tipo: "Metro cúbico (m³)", precoUnit: 95.00, fornecedor: "Mineração Central" }
];

/* ==========================================================================
   FUNÇÕES DE RENDERIZAÇÃO DE CADA ABA NO MESMO GRID DA TELA
   ========================================================================== */

function renderizarEstoque() {
  const container = document.getElementById('ordersGrid');
  const sectionTitle = document.getElementById('sectionTitle');
  const countBadge = document.getElementById('orderCount');
  
  sectionTitle.innerText = "Controle de Estoque";
  countBadge.innerText = `${dadosEstoque.length} produto(s) no estoque`;
  container.innerHTML = '';

  dadosEstoque.forEach(item => {
    const card = document.createElement('div');
    card.className = 'order-card';
    card.innerHTML = `
      <div>
        <div class="order-header">
          <span class="order-id">${item.id}</span>
          <span class="status-badge status-separacao">${item.status}</span>
        </div>
        <div class="client-info">
          <div class="client-name">${item.nome}</div>
          <div class="order-date" style="margin-top: 4px;"><strong>Categoria:</strong> ${item.categoria}</div>
          <div class="order-items" style="margin-top: 4px;"><strong>Quantidade:</strong> ${item.qtd} unidades</div>
        </div>
      </div>
      <div>
        <div class="order-price-box">
          <span class="price-label">Preço Unitário</span>
          <span class="price-value">R$ ${item.preco.toFixed(2).replace('.', ',')}</span>
        </div>
        <button class="btn-detail" onclick="alert('Editar estoque de: ${item.nome}')">
          Gerenciar Estoque <i class="fa-solid fa-pen"></i>
        </button>
      </div>
    `;
    container.appendChild(card);
  });
}

function renderizarPedidos() {
  const container = document.getElementById('ordersGrid');
  const sectionTitle = document.getElementById('sectionTitle');
  const countBadge = document.getElementById('orderCount');

  sectionTitle.innerText = "Pedidos Recebidos";
  countBadge.innerText = `${dadosPedidos.length} pedido(s) encontrado(s)`;
  container.innerHTML = '';

  dadosPedidos.forEach(pedido => {
    let statusClass = 'status-pendente';
    if (pedido.status === 'Em Separação') statusClass = 'status-separacao';
    if (pedido.status === 'Entregue') statusClass = 'status-entregue';

    const card = document.createElement('div');
    card.className = 'order-card';
    card.innerHTML = `
      <div>
        <div class="order-header">
          <span class="order-id">${pedido.id}</span>
          <span class="status-badge ${statusClass}">${pedido.status}</span>
        </div>
        <div class="client-info">
          <div class="client-name">${pedido.cliente}</div>
          <div class="order-date"><i class="fa-regular fa-clock"></i> ${pedido.data}</div>
          <div class="order-items" style="margin-top: 6px;"><strong>Itens:</strong> ${pedido.itens}</div>
        </div>
      </div>
      <div>
        <div class="order-price-box">
          <span class="price-label">Valor Total</span>
          <span class="price-value">R$ ${pedido.total.toFixed(2).replace('.', ',')}</span>
        </div>
        <button class="btn-detail" onclick="alert('Detalhes do pedido ${pedido.id}')">
          Ver detalhes <i class="fa-solid fa-arrow-right"></i>
        </button>
      </div>
    `;
    container.appendChild(card);
  });
}

function renderizarMateriais() {
  const container = document.getElementById('ordersGrid');
  const sectionTitle = document.getElementById('sectionTitle');
  const countBadge = document.getElementById('orderCount');

  sectionTitle.innerText = "Catálogo de Materiais";
  countBadge.innerText = `${dadosMateriais.length} material(is) cadastrado(s)`;
  container.innerHTML = '';

  dadosMateriais.forEach(mat => {
    const card = document.createElement('div');
    card.className = 'order-card';
    card.innerHTML = `
      <div>
        <div class="order-header">
          <span class="order-id">${mat.id}</span>
          <span class="status-badge status-pendente">Catálogo</span>
        </div>
        <div class="client-info">
          <div class="client-name">${mat.nome}</div>
          <div class="order-date" style="margin-top: 4px;"><strong>Unidade/Tipo:</strong> ${mat.tipo}</div>
          <div class="order-items" style="margin-top: 4px;"><strong>Fornecedor:</strong> ${mat.fornecedor}</div>
        </div>
      </div>
      <div>
        <div class="order-price-box">
          <span class="price-label">Preço Base</span>
          <span class="price-value">R$ ${mat.precoUnit.toFixed(2).replace('.', ',')}</span>
        </div>
        <button class="btn-detail" onclick="alert('Editar material: ${mat.nome}')">
          Editar Material <i class="fa-solid fa-gear"></i>
        </button>
      </div>    
    `;
    container.appendChild(card);
  });
}

/* ==========================================================================
   EVENTOS DE CLIQUE DOS BOTÕES SUPERIORES (ABAS)
   ========================================================================== */
document.querySelectorAll('.cat-card').forEach(btn => {
  btn.addEventListener('click', () => {
    // Remove classe ativa de todos e adiciona no clicado
    document.querySelectorAll('.cat-card').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const aba = btn.getAttribute('data-tab');

    // Alterna o conteúdo exibido embaixo de acordo com a aba escolhida
    if (aba === 'estoque') {
      renderizarEstoque();
    } else if (aba === 'pedidos') {
      renderizarPedidos();
    } else if (aba === 'materiais') {
      renderizarMateriais();
    }
  });
});

// Inicializa a página mostrando "Pedidos" por padrão (conforme estava)
renderizarPedidos();