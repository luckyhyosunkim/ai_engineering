# AI Engineering

## Grossary

- Rag: Retrieval-Augmented Generation. 문서의 정보를 가져와서 검색 결과의 정확도를 올리는 것.

## Engineering timeline

souce from [here](https://www.youtube.com/watch?v=uKbw2Lfn3wI)

1. Prompt Engineering
   - AI에게 역할을 부여하고, 원하는 답이 나오도록 지시하는 엔지니어링.
   - 하지만 이미 학습된 자료에서만 결과를 도출.
   - 따라서 2번의 context engineering으로 발전하게 된 계기.

2. Context Engineering
   - 역할과 컨텍스트(주변 맥락과 자료)를 함께 제공해서, 원하는 답이 나오도록 지시하는 엔지니어링.
   - 매번 사용자가 자료를 줘야해서 번거로움.
   - 사용자의 문서와 AI를 연결해서, AI가 직접 검색하고 필요한 정보를 직접 가져다 쓸 수 있도록 하길 원하는 것이 3번으로 발전하는 계기.

3. Harness Engineering
   - AI를 더 똑똑하게 만들기 보다는, AI가 제대로 일 할 수 있는 강제적인 환경(도구 연결, 규칙, 검증, 실수 복구)을 마련해주는 엔지니어링. ex. `CALUDE.md` file and `Hook`.
   - 매번 오류를 사람이 찾아서, 다시 지시해야하는 번거루움.
   - AI가 알아서 오류를 찾아서 수정하고, 검사하길 원하는 기능이 4번으로 발전하는 계기.

4. Loop Engineering
   - AI 스스로 '작업>검사>수정'하는 과정을, 결과물이 정해진 기준을 통과 할 때 까지, 스스로 하게 하는 엔지니어링.
     - 무엇을 성공으로 판단 할 것인가?
     - 누가 결과물을 검증 할 것인가?
       - 이를 위해, Sub-agent AI를 두고, 이는 검증만 하는 용도로 쓰기도 함. ex. main developement = Claude/ test = Codex
     - 언제 멈출 것인가?
       - ex. 모든 테스트를 통과하면 종료해. 하지만 5번 시도해도 안되면, 나에게 보고해. 같은 명령.
   - 여러 업무가 복잡하게 얽혀 있을때, 어디까지 반복 작업을 해야 할 지 모호하다는 문제점.
   - 하나의 AI가 모든 일을 다 처리하면, 초기 문제를 잘못 해석해서 중간과정이 모두 뒤틀리거나 엉뚱한 솔루션을 만들 수 도 있기 때문에, 각각의 AI가 역할을 나눠서 협업하면 될꺼라는 생각이 5번으로 발전하는 계기. ex. 시장조사를 잘못하면, 엉뚱한 상품 기획을 하게 되는 것 처럼.

5. Graph Engineereing
   - 여러 AI에게 역할을 나누는 것을 넘어서, 업무 전체가 어떤 조건과 경로로 움직일지 설계하는 엔지니어링. AI와 기존 프로그램 (검사), 사람을 모두 포함해 전체 업무의 순서와 조건, 경로를 설계하는 것.
   - ex. AI가 홈페이지를 만들면, 단순한 검사는 일반 프로그램을 쓰고, 중요한 의사결정은 사람만이 할 수 있도록 설계하는 것.

6. Reverse Engineering


## MCP
### Step-by-Step Request Flow (Host → MCP Server → Email Backend)
1. **Host (Your Python App + LLM)**: Your LLM decides it needs to send the morning digest and outputs a structured tool call (`send_message`).
2. **MCP Client (Inside Your Host)**: Your Python script's MCP client wraps that instruction in a standard JSON-RPC message over `stdio` or `HTTP` and sends it to the MCP server.
3. **MCP Server (The Translator)**: The MCP server receives the standardized MCP request, attaches your stored credentials (OAuth token or API key), and translates it into a native backend API call.  
4. **Actual Email Backend (Gmail vs. AgentMail)**:
   - Option A: **Gmail MCP Server** ("Sending a letter to yourself"):
      -  You grant the Gmail MCP Server permission (via Google OAuth login) to control your Gmail account.
      - When your Python app tells the MCP Server to send the morning news, the MCP Server calls Google's Gmail API.
      - Google's mail servers send the email from `you@gmail.com` to `you@gmail.com`.
   - *Why there's a catch*: Giving an AI full permission to send emails from your real personal account is risky (if something goes wrong, it could email anyone as you), and setting up Google OAuth tokens for a daily cron job takes extra steps.

   - Option B: **[AgentMail](https://docs.agentmail.to/welcome) MCP Server** ("Hiring an assistant with their own email address")
      - You create a separate email address for your AI bot on AgentMail, such as `my-tech-bot@agentmail.to`.
      - When your Python app tells AgentMail's MCP Server to send the morning news, AgentMail's own mail servers send the email from `my-tech-bot@agentmail.to` to `you@gmail.com`.
      - Because all email providers use the universal SMTP(Simple Mail Transfer Protocol) protocol, AgentMail's outgoing mail server delivers the message straight into your Gmail incoming mail server—just like when a friend on Naver or Outlook emails your Gmail.

      *Just as HTTP is the shared language that allows any web browser to load pages from any web server, SMTP is the shared language that allows different email providers (like AgentMail, Gmail, Naver, or Outlook) to hand off messages to one another reliably across the internet.*

## Study link

- [AI engineering from scratch](https://github.com/rohitg00/ai-engineering-from-scratch)
- [Awesome-mcp-server](https://github.com/punkpeye/awesome-mcp-servers?tab=readme-ov-file#file-systems)
- [Smithery](https://www.smithery.ai/)