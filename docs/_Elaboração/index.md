# Especificação da API REST - FitLife
## Visão Geral da API
A API FitLife segue os princípios REST e oferece endpoints organizados por
recursos principais. Todos os endpoints retornam dados em formato JSON e
utilizam códigos de status HTTP padrão.
### Base URL
http://localhost:/api/v/
### Autenticação
A API utiliza autenticação JWT (JSON Web Tokens). Inclua o token no header:
Authorization: Bearer
## Endpoints por Recurso
### 1. Autenticação
#### POST /auth/registro/
Registra novo usuário na plataforma.
**Request Body:**
```json
{
"username": "joao_silva",
"email": "joao@email.com",
"first_name": "João",
"last_name": "Silva",
"password": "senha123456",
"password_confirm": "senha123456"
}
Response ():
{
"message": "Usuário criado com sucesso",
"user": {
"id": 1,
"username": "joao_silva",
"email": "joao@email.com",
"nome_completo": "João Silva"
}
}
POST /auth/login/
Autentica usuário e retorna token JWT.
Request Body:
{
"email": "joao@email.com",
"password": "senha123456"
}
Response ():
{
"message": "Login realizado com sucesso",
"user": {
"id": 1,
"username": "joao_silva",
"email": "joao@email.com",
"nome_completo": "João Silva"
},
"tokens": {
"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
}
. Usuários
GET /usuarios/perfil/
Retorna perfil do usuário autenticado.
Response ():
{
"id": 1,
"username": "joao_silva",
"email": "joao@email.com",
"first_name": "João",
"last_name": "Silva",
"data_nascimento": "1990-05-15",
"altura": 1.75,
"peso_atual": 70.5,
"objetivo_principal": "ganho_massa",
"nivel_experiencia": "intermediario",
"imc": 23.02,
"idade": 33
}


PUT /usuarios/perfil/
Atualiza perfil do usuário autenticado.
. Exercícios
GET /exercicios/
Lista exercícios com paginação e filtros.
Query Parameters: - grupo_muscular : Filtrar por grupo muscular - equipamento :
Filtrar por equipamento necessário - nivel : Filtrar por nível de dificuldade - search :
Busca textual por nome ou descrição - page : Número da página - page_size : Itens
por página
Response ():
{
"count": 150,
"next": "http://localhost:8000/api/v1/exercicios/?page=2",
"previous": null,
"results": [
{
"id": 1,
"nome": "Flexão de Braço",
"descricao": "Exercício clássico para peitoral e tríceps",
"grupo_muscular_principal": "peito",
"equipamento_necessario": "peso_corporal",
"nivel_dificuldade": "iniciante",
"calorias_por_minuto": 8.5,
"tempo_execucao_medio": 15
}
]
}
POST /exercicios/
Cria novo exercício (usuários autenticados).
GET /exercicios/{id}/
Retorna detalhes de exercício específico.
. Treinos
GET /treinos/
Lista treinos do usuário autenticado.
Response ():
{
"count": 5,
"results": [
{
"id": 1,
"nome": "Treino Push Iniciante",
"descricao": "Treino focado em empurrar para iniciantes",
"objetivo": "ganho_massa",
"nivel_dificuldade": "iniciante",
"duracao_estimada": 45,
"calorias_estimadas": 320,
"exercicios_count": 6,
"data_criacao": "2024-01-15T10:30:00Z"
}
]
}
POST /treinos/
Cria novo treino.
Request Body:
{
"nome": "Treino Upper Body",
"descricao": "Treino para parte superior do corpo",
"objetivo": "ganho_massa",
"nivel_dificuldade": "intermediario",
"publico": false,
"exercicios": [
{
"exercicio_id": 1,
"ordem": 1,
"series": 4,
"repeticoes": 8,
"carga": 20.0,
"tempo_descanso": 90
},
{
"exercicio_id": 2,
"ordem": 2,
"series": 3,
"repeticoes": 12,
"tempo_descanso": 60
}
]
}

GET /treinos/{id}/
Retorna detalhes completos do treino.
PUT /treinos/{id}/
Atualiza treino existente.
DELETE /treinos/{id}/
Remove treino.
POST /treinos/{id}/duplicar/
Cria cópia do treino.
. Playlists
GET /playlists/
Lista playlists do usuário.
POST /playlists/
Cria nova playlist.
Request Body:
{
"nome": "Programa Iniciante 4 Semanas",
"descricao": "Programa completo para iniciantes",
"objetivo": "geral",
"duracao_programa": 28,
"nivel_dificuldade": "iniciante",
"publico": false,
"treinos": [
{
"treino_id": 1,
"ordem": 1,
"dia_semana": "segunda"
},
{
"treino_id": 2,
"ordem": 2,
"dia_semana": "quarta"
}
]
}
GET /playlists/{id}/
Detalhes da playlist com treinos.
PUT /playlists/{id}/
Atualiza playlist.
DELETE /playlists/{id}/
Remove playlist.
Códigos de Status HTTP
Código Significado Uso
 OK Requisição bem-sucedida
 Created Recurso criado com sucesso
 Bad Request Dados inválidos na requisição
 Unauthorized Token inválido ou ausente
 Forbidden Sem permissão para acessar recurso
 Not Found Recurso não encontrado
 Internal Server Error Erro interno do servidor

Tratamento de Erros
Todas as respostas de erro seguem o formato padrão:
{
"error": "Descrição do erro",
"details": {
"campo": ["Mensagem específica do campo"]
}
}
