# ⚛️ Tabela Periódica Interativa (TCC)

Tabela periódica com os **118 elementos**, feita como TCC. Clique em qualquer elemento para ver as informações dele e o **modelo atômico de Bohr** desenhado com as camadas de elétrons.

🔗 **Acesse:** [tcc-tabela-periodica.vercel.app](https://tcc-tabela-periodica.vercel.app)

## Funcionalidades

- **Os 118 elementos** posicionados no lugar certo da tabela (período e grupo)
- **Cores por família**: metais alcalinos, alcalinos terrosos, metais de transição, outros metais, metaloides, não-metais, halogênios, gases nobres, lantanídeos e actinídeos (com legenda)
- **Detalhes do elemento** em uma janela: nome, símbolo, número atômico, massa atômica e família
- **Distribuição eletrônica** por camadas (K, L, M, N, O, P, Q)
- **Modelo de Bohr** desenhado na hora, com o núcleo e os elétrons em cada camada
- Layout responsivo

## Como funciona

O back-end em **Flask** guarda os dados dos 118 elementos e oferece uma pequena API. O front busca os dados com `fetch`, monta a tabela e desenha o modelo atômico.

| Rota | O que retorna |
| --- | --- |
| `GET /` | A página da tabela |
| `GET /api/elementos` | Lista de todos os elementos com posição na tabela |
| `GET /api/elemento/<numero>` | Detalhes de um elemento e suas camadas eletrônicas |

**Exemplo:** `GET /api/elemento/1`

```json
{
  "nome": "Hidrogênio",
  "simbolo": "H",
  "massa_atomica": "1.008",
  "grupo": "Não-metal",
  "camadas_eletronicas": [{ "camada": "K", "eletrons": 1, "nivel": 1 }],
  "configuracao": "K: 1",
  "total_eletrons": 1
}
```

## Tecnologias

- **Python + Flask** (back-end e API)
- **Flask-CORS**
- **HTML, JavaScript e Tailwind CSS** (interface)
- **Vercel** (hospedagem)

## Estrutura

```
├── app.py               # dados dos 118 elementos e rotas da API
├── templates/
│   └── index.html       # tabela, janela de detalhes e modelo de Bohr
├── requirements.txt
└── vercel.json          # configuração do deploy
```

## Como rodar localmente

```bash
git clone https://github.com/julio-aurelio/TCC-tabela-periodica-.git
cd TCC-tabela-periodica-
pip install -r requirements.txt
python app.py
```

Depois abra `http://127.0.0.1:5000` no navegador.

---

Feito por **Julio Aurelio Souza** 😼
