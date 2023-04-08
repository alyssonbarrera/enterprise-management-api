# API

Enterprise Management API

## Requisitos Funcionais

- [x] Deve ser possível cadastrar um departamento;  
- [x] Deve ser possível consultar informações de um departamento;  
- [x] Deve ser possível consultar todos os departamentos;  
- [x] Deve ser possível atualizar um departamento;  
- [x] Deve ser possível deletar um departamento;  
- [x] Deve ser possível cadastrar um funcionário;  
- [ ] Deve ser possível consultar informações de um funcionário;  
- [ ] Deve ser possível consultar todos os funcionários;  
- [ ] Deve ser possível atualizar um funcionário;  
- [ ] Deve ser possível deletar um funcionário;  
- [ ] Deve ser possível cadastrar um projeto;  
- [ ] Deve ser possível consultar um projeto;  
- [ ] Deve ser possível consultar todos os projetos;  
- [ ] Deve ser possível atualizar um projeto;  
- [ ] Deve ser possível deletar um projeto.  

## Regras de Negócio

- [x] Não deve ser possível cadastrar um departamento com nome duplicado;  
- [ ] Não deve ser possível deletar um departamento se houver projeto ativo;  
- [ ] Não deve ser possível um funcionário supervisionar ou trabalhar em um projeto que exceda sua carga horária;  
- [x] Não deve ser possível cadastrar um funcionário caso já exista um funcionário com mesmo nome, cpf ou rg.  


## Requisitos Não-funcionais

- [x] Os dados da aplicação precisam estar persistidos em um banco MySQL;  
- [x] Todas as listas de dados precisam estar paginadas com 20 itens por página;  
- [x] A API deve conter testes automatizados;  
- [ ] A API deve estar documentada.  