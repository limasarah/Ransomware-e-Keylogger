🦠 Simulação de Malware em Python
Ransomware e Keylogger em Ambiente Controlado
📌 Visão Geral

Este projeto apresenta a simulação controlada de comportamentos típicos de malware utilizando Python, com foco em dois vetores amplamente explorados em incidentes de segurança: ransomware e keylogger.

A iniciativa tem como objetivo demonstrar, de forma prática, como essas ameaças operam, quais riscos representam para o ambiente corporativo e quais controles podem ser aplicados para prevenção, detecção e resposta.

Todos os testes foram conduzidos em ambiente isolado, sem qualquer interação com sistemas reais.

🎯 Objetivos
Demonstrar o funcionamento prático de ransomware e keylogger
Simular técnicas de comprometimento de dados e captura de informações
Avaliar riscos associados a execução de scripts maliciosos
Reforçar a importância de controles de segurança em endpoints
Documentar evidências técnicas com abordagem estruturada
Mapear estratégias de mitigação alinhadas a boas práticas
🧪 Ambiente de Execução

O projeto foi desenvolvido em ambiente controlado, garantindo isolamento e segurança durante os testes.

Linguagem: Python 3
Execução local com arquivos simulados
Ambiente isolado (laboratório virtual)
Dados utilizados exclusivamente para teste

🔐 Simulação de Ransomware
📍 Contexto

O cenário de ransomware foi desenvolvido para demonstrar o impacto da indisponibilidade de dados causada por criptografia maliciosa, um dos principais vetores de ataque em ambientes corporativos.

⚙️ Implementação

A simulação contempla:

Criação de arquivos de teste
Script de criptografia dos arquivos
Geração de arquivo contendo chave/senha utilizada
Substituição dos arquivos originais por versões criptografadas
Exibição de mensagem simulando solicitação de resgate
Implementação de script dedicado à descriptografia
📂 Componentes
Módulo de criptografia
Arquivo de controle de chave (key.txt)
Módulo de descriptografia
Arquivos de teste
🔎 Análise

O cenário evidencia como a ausência de controles de segurança pode resultar em indisponibilidade de dados críticos, reforçando a necessidade de estratégias robustas de backup e proteção de arquivos.
⌨️ Simulação de Keylogger
📍 Contexto

O keylogger foi projetado para demonstrar a captura silenciosa de dados sensíveis, um dos métodos mais utilizados para obtenção de credenciais em ataques direcionados.

⚙️ Implementação

O funcionamento inclui:

Captura de eventos de teclado em tempo real
Registro contínuo das entradas do usuário
Armazenamento em arquivo local (.txt)
Execução em segundo plano
Configuração do script com extensão .pyw, permitindo execução sem interface visível ao usuário
Simulação de envio automatizado das informações capturadas
🔎 Análise

A utilização da extensão .pyw evidencia como processos podem ser executados de forma silenciosa no endpoint, dificultando a detecção por usuários e reforçando a necessidade de monitoramento de comportamento e controle de execução de aplicações.

📊 Principais Riscos Observados
Comprometimento de confidencialidade (captura de credenciais)
Perda de disponibilidade de dados (criptografia maliciosa)
Execução silenciosa de scripts sem percepção do usuário
Dependência do fator humano como vetor de ataque
🛡️ Controles e Mitigações Recomendadas

Com base nos cenários simulados:

🔐 Proteção de Endpoint
Soluções de antivírus/EDR com análise comportamental
Restrição de execução de scripts não autorizados
Monitoramento contínuo de processos
🌐 Segurança de Rede
Uso de firewall e controle de tráfego
Inspeção de conexões suspeitas
💾 Proteção de Dados
Políticas de backup periódico
Armazenamento seguro e segregado
👤 Fator Humano
Treinamento de conscientização em segurança
Políticas de uso seguro de sistemas
🧪 Análise e Prevenção
Uso de sandbox para análise de arquivos
Auditoria e monitoramento de logs
📚 Competências Demonstradas
Programação em Python aplicada à cibersegurança
Análise prática de comportamento de malware
Simulação de ataques em ambiente controlado
Avaliação de riscos e impactos
Estruturação de documentação técnica
Visão integrada entre ataque e defesa.
⚠️ Considerações Éticas:

Este projeto foi desenvolvido exclusivamente para fins educacionais, em ambiente controlado e sem qualquer interação com sistemas reais.

As técnicas demonstradas têm como objetivo promover conscientização e aprimoramento em segurança da informação.

🚀 Evoluções Futuras:
Implementação de criptografia avançada,
Simulação de persistência em sistema,
Integração com cenários de detecção (EDR/SIEM),
Simulação de comunicação com servidor controlado (C2),
Expansão para outros tipos de malware.
