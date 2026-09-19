# PROJECT_AI.md - compact example

> Это **пример**, а не второй набор правил методики. Скопируйте только полезные поля и замените значения на факты своего проекта.

```text
Project: ExampleOrders
CoordinationScope: whole repository
OwningCoordinator: Coordinator Main

AuthoritativeSource: EDT project ./ExampleOrders
ExecutionProfile: .1c-ai/profiles/1c-edt-mcp/PROFILE.md

AcceptedCheckpoint: git:<exact accepted project SHA>
MethodologyPackage: Megabonstr/1c-ai-development-methodology @ <exact pinned upstream SHA>

Knowledge:
- docs/architecture.md
- docs/integrations.md

ArchitectureInvariants:
- preserve existing public integration contracts
- preserve current-user rights/RLS

DO_NOT_TOUCH:
- production infobase

Runtime/VerificationHandles:
- test infobase: <exact local/test handle>
- focused tests: <path/command or NOT_USED>

OpenMaterialUnknowns:
- <none, or one exact material unknown>
```

## Как читать пример

- **Project** - короткая идентичность проекта.
- **CoordinationScope** - чем владеет текущий Coordinator Main: весь проект или одна чёткая область.
- **OwningCoordinator** - один владелец координационных решений для этой области.
- **AuthoritativeSource** - где реально находятся канонические исходники.
- **ExecutionProfile** - EDT + MCP или XML + Configurator, выбранный по authoritative source.
- **AcceptedCheckpoint** - точный принятый SHA/состояние проекта.
- **MethodologyPackage** - какой exact snapshot `1c-ai-development` установлен в проект.
- **Knowledge** - точные документы/индексы, а не вставленная копия их содержимого.
- **ArchitectureInvariants / DO_NOT_TOUCH** - только действительно материальные проектные ограничения; не перечисляйте всё, что просто находится вне текущего scope.
- **Runtime/VerificationHandles** - точные handles тестовой среды и проверок, если они стабильны и полезны.
- **OpenMaterialUnknowns** - только существенные открытые неизвестные.

Для XML-проекта замените, например:

```text
AuthoritativeSource: XML source ./src
ExecutionProfile: .1c-ai/profiles/1c-xml-configurator/PROFILE.md
```

`PROJECT_AI.md` принадлежит проекту. Не копируйте в него содержимое `.1c-ai/core/*`, историю Issues или полные чаты.
