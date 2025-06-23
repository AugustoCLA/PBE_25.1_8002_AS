
## Atores do Sistema
### Ator Primário: Usuário
**Descrição:** Pessoa interessada em fitness que utiliza a plataforma para
criar e gerenciar treinos.
**Responsabilidades:**
- Gerenciar seu perfil pessoal
- Criar e personalizar treinos
- Organizar treinos em playlists
- Buscar exercícios no catálogo
### Ator Secundário: Administrador
**Descrição:** Responsável pela manutenção do catálogo de exercícios e gestão
geral do sistema.
**Responsabilidades:**
- Gerenciar catálogo de exercícios
- Moderar conteúdo da plataforma
- Monitorar uso do sistema
- Manter qualidade dos dados
## Caso de Uso 1: Cadastro e Autenticação de Usuário
### Identificação
- **ID:** UC001
- **Nome:** Cadastro e Autenticação de Usuário
- **Ator Principal:** Usuário
- **Objetivo:** Permitir que novos usuários se cadastrem e usuários existentes
façam login
### Descrição
Este caso de uso permite que uma pessoa interessada em fitness se cadastre na
plataforma FitLife, fornecendo suas informações pessoais e de fitness, e
posteriormente faça login para acessar as funcionalidades do sistema.
### Pré-condições
- Usuário possui acesso à internet
- Usuário possui email válido
- Sistema está disponível e funcionando
### Fluxo Principal
1. Usuário acessa a tela de cadastro
2. Sistema exibe formulário de cadastro
3. Usuário preenche informações obrigatórias:
- Nome completo
- Email único
- Senha segura
- Data de nascimento
4. Usuário preenche informações de fitness (opcional):
- Altura e peso atual
- Objetivos principais
- Nível de experiência
5. Sistema valida dados fornecidos
6. Sistema cria conta do usuário
7. Sistema envia confirmação de cadastro
8. Usuário faz login com email e senha
9. Sistema autentica credenciais
10. Sistema gera token JWT
11. Sistema retorna token e dados do usuário
12. Usuário acessa dashboard principal
### Fluxos Alternativos
**A1 - Email já cadastrado:**
- 5a. Sistema detecta email duplicado
- 5b. Sistema exibe mensagem de erro
- 5c. Usuário corrige email ou faz login
**A2 - Senha não atende critérios:**
- 5a. Sistema valida força da senha
- 5b. Sistema exibe critérios não atendidos
- 5c. Usuário cria nova senha
**A3 - Login com credenciais inválidas:**
- 9a. Sistema não encontra usuário ou senha incorreta
- 9b. Sistema exibe mensagem de erro genérica
- 9c. Usuário tenta novamente ou recupera senha
### Pós-condições
- Usuário possui conta ativa no sistema
- Usuário está autenticado com token válido
- Usuário pode acessar funcionalidades da plataforma
### Regras de Negócio
- Email deve ser único no sistema
- Senha deve ter mínimo 8 caracteres
- Token JWT expira em 24 horas
- Dados pessoais são opcionais exceto nome e email
## Caso de Uso 2: Criação de Treino Personalizado
### Identificação
- **ID:** UC002
- **Nome:** Criação de Treino Personalizado
- **Ator Principal:** Usuário
- **Objetivo:** Permitir que usuário crie treino personalizado selecionando
exercícios
### Descrição
Este caso de uso permite que um usuário autenticado crie um treino
personalizado, selecionando exercícios do catálogo disponível, definindo
parâmetros específicos como séries, repetições e carga, e organizando a
sequência de execução.
### Pré-condições
- Usuário está autenticado no sistema
- Catálogo de exercícios possui itens disponíveis
- Usuário possui permissão para criar treinos
### Fluxo Principal
1. Usuário acessa seção de criação de treinos
2. Sistema exibe formulário de novo treino
3. Usuário define informações básicas:
- Nome do treino
- Descrição/objetivo
- Nível de dificuldade
4. Usuário acessa catálogo de exercícios
5. Sistema exibe exercícios com filtros disponíveis
6. Usuário aplica filtros (grupo muscular, equipamento)
7. Sistema filtra e exibe exercícios relevantes
8. Usuário seleciona exercício desejado
9. Sistema exibe formulário de parâmetros:
- Número de séries
- Repetições por série
- Carga/peso (se aplicável)
- Tempo de descanso
10. Usuário define parâmetros do exercício
11. Sistema adiciona exercício ao treino
12. Usuário repete passos 8-11 para outros exercícios
13. Usuário organiza ordem dos exercícios
14. Sistema calcula duração estimada do treino
15. Usuário salva treino criado
16. Sistema valida e armazena treino
17. Sistema confirma criação com sucesso
### Fluxos Alternativos
**A1 - Busca por exercício específico:**
- 6a. Usuário utiliza busca textual
- 6b. Sistema busca por nome/descrição
- 6c. Sistema exibe resultados da busca
**A2 - Remoção de exercício do treino:**
- 12a. Usuário decide remover exercício
- 12b. Sistema remove exercício da lista
- 12c. Sistema recalcula duração estimada
**A3 - Treino sem exercícios:**
- 15a. Usuário tenta salvar treino vazio
- 15b. Sistema exibe erro de validação
- 15c. Usuário adiciona pelo menos um exercício
### Pós-condições
- Treino é criado e associado ao usuário
- Treino está disponível na lista de treinos do usuário
- Usuário pode editar, duplicar ou usar o treino
### Regras de Negócio
- Treino deve ter pelo menos um exercício
- Parâmetros numéricos devem ser positivos
- Usuário só pode editar seus próprios treinos
- Duração é calculada automaticamente
## Caso de Uso 3: Gestão de Playlist de Treinos
### Identificação
- **ID:** UC003
- **Nome:** Gestão de Playlist de Treinos
- **Ator Principal:** Usuário
- **Objetivo:** Permitir organização de treinos em playlists temáticas
### Descrição
Este caso de uso permite que um usuário autenticado organize seus treinos
criados em playlists temáticas, facilitando o planejamento de rotinas de
exercícios e programas de treinamento estruturados.
### Pré-condições
- Usuário está autenticado no sistema
- Usuário possui pelo menos um treino criado
- Sistema possui funcionalidade de playlists ativa
### Fluxo Principal
1. Usuário acessa seção de playlists
2. Sistema exibe playlists existentes do usuário
3. Usuário seleciona "Criar Nova Playlist"
4. Sistema exibe formulário de criação:- Nome da playlist
- Descrição/objetivo
- Nível de dificuldade
- Duração do programa (dias/semanas)
5. Usuário preenche informações da playlist
6. Sistema cria playlist vazia
7. Usuário acessa lista de treinos disponíveis
8. Sistema exibe treinos do usuário
9. Usuário seleciona treino para adicionar
10. Sistema exibe opções de agendamento:
- Dia da semana
- Ordem na sequência
- Observações específicas
11. Usuário define parâmetros do treino na playlist
12. Sistema adiciona treino à playlist
13. Usuário repete passos 9-12 para outros treinos
14. Usuário organiza ordem dos treinos na playlist
15. Sistema calcula estatísticas da playlist:
- Duração total estimada
- Grupos musculares trabalhados
- Distribuição de dificuldade
16. Usuário salva playlist completa
17. Sistema valida e armazena playlist
18. Sistema confirma criação com sucesso
### Fluxos Alternativos
**A1 - Edição de playlist existente:**
- 3a. Usuário seleciona playlist existente
- 3b. Sistema carrega dados da playlist
- 3c. Usuário modifica informações ou treinos
- 3d. Sistema salva alterações
**A2 - Remoção de treino da playlist:**
- 13a. Usuário decide remover treino
- 13b. Sistema remove treino da playlist
- 13c. Sistema recalcula estatísticas
**A3 - Duplicação de playlist:**
- 3a. Usuário seleciona "Duplicar Playlist"
- 3b. Sistema cria cópia da playlist
- 3c. Usuário pode modificar a cópia
**A4 - Compartilhamento de playlist:**
- 16a. Usuário marca playlist como pública
- 16b. Sistema gera link de compartilhamento
- 16c. Outros usuários podem visualizar playlist
### Pós-condições
- Playlist é criada e associada ao usuário
- Treinos estão organizados na sequência definida
- Usuário pode seguir programa estruturado
- Estatísticas da playlist estão disponíveis
### Regras de Negócio
- Playlist deve ter pelo menos um treino
- Treinos podem aparecer em múltiplas playlists
- Ordem dos treinos pode ser reorganizada
- Playlists podem ser marcadas como públicas ou privadas
- Estatísticas são calculadas automaticamente
