## Diagrama UML em PlantUML
```plantuml
@startuml FitLife_Classes
!define ENTITY class
!define ENUM enum
' Configurações de estilo
skinparam class {
BackgroundColor LightBlue
BorderColor DarkBlue
ArrowColor DarkBlue
}
' Entidade Usuario
ENTITY Usuario {
+id: Integer {PK}
+username: String {unique}
+email: String {unique}
+first_name: String
+last_name: String
+password: String {hashed}
+data_nascimento: Date
+genero: String
+altura: Float
+peso_atual: Float
+objetivo_principal: String
+nivel_experiencia: String
+bio: Text
+date_joined: DateTime
+data_ultima_atividade: DateTime
--
+get_full_name(): String
+calcular_imc(): Float
+get_idade(): Integer
}
' Entidade Exercicio
ENTITY Exercicio {
+id: Integer {PK}
+nome: String {unique}
+descricao: Text
+grupo_muscular_principal: String
+grupos_musculares_secundarios: String
+equipamento_necessario: String
+nivel_dificuldade: String
+instrucoes_execucao: Text
+calorias_por_minuto: Float
+tempo_execucao_medio: Integer
+publico: Boolean
+criado_por: Usuario {FK}
+data_criacao: DateTime
+ativo: Boolean
--
+get_grupos_musculares(): List
+calcular_calorias_total(): Float
}
' Entidade Treino
ENTITY Treino {
+id: Integer {PK}
+nome: String
+descricao: Text
+objetivo: String
+nivel_dificuldade: String
+duracao_estimada: Integer
+calorias_estimadas: Float
+publico: Boolean
+criado_por: Usuario {FK}
+data_criacao: DateTime
+data_modificacao: DateTime
--
+calcular_duracao(): Integer
+calcular_calorias(): Float
+get_grupos_musculares(): List
+duplicar(): Treino
}
' Entidade TreinoExercicio (Relacionamento N:M)
ENTITY TreinoExercicio {
+id: Integer {PK}
+treino: Treino {FK}
+exercicio: Exercicio {FK}
+ordem: Integer
+series: Integer
+repeticoes: Integer
+carga: Float
+tempo_descanso: Integer
+observacoes: Text
--
+calcular_volume(): Float
+get_tempo_total(): Integer
}
' Entidade Playlist
ENTITY Playlist {
+id: Integer {PK}
+nome: String
+descricao: Text
+objetivo: String
+duracao_programa: Integer
+nivel_dificuldade: String
+publico: Boolean
+criado_por: Usuario {FK}
+data_criacao: DateTime
+data_modificacao: DateTime
--
+calcular_duracao_total(): Integer
+get_treinos_ordenados(): List
+duplicar(): Playlist
}
' Entidade PlaylistTreino (Relacionamento N:M)
ENTITY PlaylistTreino {
+id: Integer {PK}
+playlist: Playlist {FK}
+treino: Treino {FK}
+ordem: Integer
+dia_semana: String
+observacoes: Text
--
+get_proximo_treino(): Treino
}
' Relacionamentos
Usuario ||--o{ Exercicio : "cria"
Usuario ||--o{ Treino : "cria"
Usuario ||--o{ Playlist : "cria"
Treino ||--o{ TreinoExercicio : "contém"
Exercicio ||--o{ TreinoExercicio : "usado em"
Playlist ||--o{ PlaylistTreino : "contém"
Treino ||--o{ PlaylistTreino : "incluído em"
@enduml
