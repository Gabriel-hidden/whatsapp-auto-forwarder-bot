**WhatsApp Auto Forwarder - Leia-me**

### Visão Geral

Este script em Python, criado por Gabriel Ferreira de França, automatiza interações no WhatsApp usando Selenium. O bot pode enviar mensagens predefinidas para contatos específicos e encaminhar mensagens recebidas. Sua integração perfeita com o WhatsApp Web simplifica interações, proporcionando uma maneira conveniente de gerenciar mensagens.

### Requisitos

Certifique-se de ter o Python e o gerenciador de pacotes pip instalados. Instale as bibliotecas necessárias com:

```bash
pip install selenium webdriver_manager pyperclip
```

### Funcionalidades

1. **Envio Automático de Mensagens:**
   - Personalize e envie mensagens predefinidas para uma lista específica de contatos.

2. **Encaminhamento de Mensagens:**
   - Encaminhe automaticamente mensagens recebidas para uma lista pré-definida de contatos.

3. **Automação do WhatsApp Web:**
   - Interaja com o WhatsApp Web usando Selenium para uma experiência perfeita.

### Personalização

- **Conteúdo das Mensagens:**
  - Personalize as mensagens no código-fonte modificando a variável `mensagem`.

- **Lista de Contatos:**
  - Adicione ou remova contatos na lista `contatos` conforme necessário.
  - 
### Autor

- **Gabriel Ferreira de França**

### Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE] para obter detalhes.

### Observações

- **Esperas Explícitas:**
  - O script utiliza esperas explícitas para garantir que os elementos estejam presentes antes de interagir com eles.

- **Constantes Xpath:**
  - Os caminhos Xpath para os elementos do WhatsApp Web foram definidos como constantes para facilitar modificações.

- **Evitar Sleeps Fixos:**
  - O código procura minimizar o uso de `sleep` com durações fixas, preferindo esperas explícitas.

---
