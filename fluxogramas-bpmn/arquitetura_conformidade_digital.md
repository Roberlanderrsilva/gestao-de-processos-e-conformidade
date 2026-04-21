## 🏛️ Arquitetura de Software: Compliance-by-Design

Este documento descreve as premissas de Engenharia de Software adotadas para garantir que o sistema seja inerentemente conforme às normas de Direito Administrativo.

## 1. Pilares da Arquitetura
* **Imutabilidade de Logs:** Utilização de logs estruturados (JSON) para garantir que toda ação administrativa seja rastreável e não editável.
* **Desacoplamento de Regras de Negócio:** As regras da Lei 14.133/21 são tratadas como microserviços de validação independentes.
* **Security-First:** Camadas de segurança baseadas em OAuth2 e JWT para garantir que apenas agentes públicos autorizados acessem dados sensíveis.

## 2. Fluxo de Integração de Dados (Interoperabilidade)
O sistema foi desenhado para se comunicar com o **PNCP** através de mensageria assíncrona, garantindo que mesmo em quedas de sistema, a transparência pública não seja comprometida.

## 3. Stack Tecnológica Sugerida
* **Backend:** Java Spring Boot ou Python (FastAPI) - pela robustez em processos lógicos.
* **Banco de Dados:** PostgreSQL com extensões de auditoria.
* **Infraestrutura:** Containers Docker orquestrados em Kubernetes para alta disponibilidade.
