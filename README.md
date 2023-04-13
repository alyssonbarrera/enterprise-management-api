# API

Enterprise Management API

## Department  
### Requisitos Funcionais  
- [x] Deve ser possível cadastrar um departamento;  
- [x] Deve ser possível consultar informações de um departamento;  
- [x] Deve ser possível consultar todos os departamentos;  
- [x] Deve ser possível atualizar um departamento;  
- [x] Deve ser possível deletar um departamento.  

### Regras de Negócio  
- [x] Não deve ser possível cadastrar um departamento com nome duplicado;  
- [x] Não deve ser possível deletar um departamento se houver projeto ativo;  
- [x] Não deve ser possível deletar um departamento se houver funcionários ativos.  

## Employee  
### Requisitos Funcionais  
- [x] Deve ser possível cadastrar um funcionário;  
- [x] Deve ser possível consultar informações de um funcionário;  
- [x] Deve ser possível consultar todos os funcionários;  
- [x] Deve ser possível atualizar um funcionário;  
- [x] Deve ser possível deletar um funcionário.  

### Regras de Negócio  
- [x] Não deve ser possível cadastrar um funcionário caso já exista um funcionário com mesmo nome, cpf ou rg;  
- [x] Não deve ser possível um funcionário supervisionar ou trabalhar em um projeto que exceda sua carga horária.  

## Project  
### Requisitos Funcionais  
- [x] Deve ser possível cadastrar um projeto;  
- [x] Deve ser possível consultar um projeto;  
- [x] Deve ser possível consultar todos os projetos;  
- [x] Deve ser possível atualizar um projeto;  
- [x] Deve ser possível deletar um projeto;  
- [x] Deve ser possível substituir todos os funcionários do projeto;  
- [x] Deve ser possível adicionar funcionários a um projeto;  
- [x] Deve ser possível remover funcionários de um projeto;  
- [x] Deve ser possível obter as estatísticas do projeto;  
- [x] Deve ser possível marcar um projeto como concluído.   

### Regras de Negócio  
- [x] A quantidade de horas necessárias para a conclusão do projeto deve ser calculada com base na quantidade de horas concluídas pelos funcionários e no número de horas restantes;  
- [x] A quantidade de horas realizadas no projeto deve ser baseada na quantidade de horas trabalhadas pelos funcionários e no número de semanas passadas desde o último cálculo;  
- [x] Não deve ser possível adicionar um funcionário ou supervisor em um projeto caso eles não tenham horas disponíveis;  
- [x] Os funcionários devem ser desassociados do projeto ao marcá-lo como concluído.  

### Requisitos Não-funcionais
- [x] Os dados da aplicação precisam estar persistidos em um banco MySQL;  
- [x] Todas as listas de dados precisam estar paginadas com 20 itens por página;  
- [x] A API deve conter testes automatizados;  
- [x] A API deve conter documentação.  

---

Documentação: https://documenter.getpostman.com/view/20700565/2s93XwyPMz  

---

### 💻 Para rodar em sua máquina, siga os passos abaixo:  

<br/>

📄 Clone o projeto em sua máquina;  
📂Abra o terminal na pasta do projeto e rode o seguinte comando:  

```shell
python -m venv venv
 ```

⌨ Após, rode o seguinte comando se estiver usando Mac ou Linux:  

```shell
source venv/bin/activate
```

💻 Caso esteja no Windows, use:  

```shell
.\venv\Scripts\activate
```

⌨ Em seguinda, rode o comando:  

```shell
pip install -r requirements.txt
```

🚢 Após, rode o comando:

```shell
docker-compose up
```

⏳ Aguarde até que o container esteja em execução;  

🔐 Antes de prosseguir, é necessário criar o arquivo .env na raiz do projeto;  

📄 Uma vez criado, ele deverá conter:

```
DATABASE_NAME=database
DATABASE_USER=docker
DATABASE_PASSWORD=docker
DATABASE_HOST=localhost
DATABASE_PORT=3306
```

📡 Em seguida, rode o comando a seguir caso queira inicializar o servidor:  

```shell
python manage.py runserver
```

🧪 Caso queira executar os testes, use:  

```shell
python manage.py test
```

---

## Techs

<div>
    <img width=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />
    <img width=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" />
    <img width=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" />
    <img width=30 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-plain.svg" />
</div>