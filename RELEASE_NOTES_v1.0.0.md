# v1.0.0 - первый публичный релиз

Дата: 2026-09-19

`1c-ai-development-methodology` - переносимая методика и пакет машинных инструкций для 1С-разработки с AI-агентами.

## Что входит в v1.0.0

- человеческая документация на русском;
- machine-facing пакет `.1c-ai/**`;
- skills `.agents/skills/1c-ai-*/**`;
- профили для EDT + MCP и XML + Конфигуратор;
- Task Contract, Source First, Token Diet, evidence/verification, orchestration и closeout;
- manual pinned adoption;
- Git/GitHub рекомендуемый flow;
- практический деградированный маршрут без Git;
- validator и GitHub templates;
- правила публичной обратной связи.

## Что проверено перед публикацией

- независимый критический аудит release candidate: PASS после двух ограниченных коррекций;
- контрольный прогон на чистом private fixture:
  - Test A - PASS: пустой repo -> подключение пакета -> PROJECT_AI -> bounded 1C source task -> feature -> preprod -> main;
  - Test B - PASS: alternate Coordinator placement с Google Doc как durable task carrier и GitHub только как source/delivery transport;
- public export hygiene scan;
- validator в новом публичном repository: PASS.

## Известные ограничения

v1.0.0 - первый публичный релиз. В методике, документации и отдельных сценариях могут оставаться неточности, ошибки и несовместимости.

Сейчас не поставляются:

- детерминированный installer/update/uninstall - см. [Issue #2](https://github.com/Megabonstr/1c-ai-development-methodology/issues/2);
- собственный Gitless durable-state backend - см. [Issue #1](https://github.com/Megabonstr/1c-ai-development-methodology/issues/1);
- универсальный live 1C read-only runtime reader - см. [Issue #4](https://github.com/Megabonstr/1c-ai-development-methodology/issues/4).

Контрольный fixture доказал SOURCE/static-level workflow, но не заменяет реальный 1С BUILD/DEPLOY/RUNTIME/NATIVE evidence.

## Roadmap после v1.0.0

- [#1 Gitless durable state](https://github.com/Megabonstr/1c-ai-development-methodology/issues/1)
- [#2 deterministic installer/update/uninstall](https://github.com/Megabonstr/1c-ai-development-methodology/issues/2)
- [#3 deeper public 1C cases](https://github.com/Megabonstr/1c-ai-development-methodology/issues/3)
- [#4 read-only live 1C data access](https://github.com/Megabonstr/1c-ai-development-methodology/issues/4)
- [#5 public adoption reports and counterexamples](https://github.com/Megabonstr/1c-ai-development-methodology/issues/5)

## Лицензии

- machine/executable methodology layer - MPL-2.0;
- README/docs/research/examples/source registry - CC BY-SA 4.0.

См. [LICENSE](LICENSE) и [NOTICE.md](NOTICE.md).

## Обратная связь

Если вы нашли ошибку, противоречие, несовместимость, лишнюю бюрократию или реальный контрпример - создайте Issue по [правилам обратной связи](CONTRIBUTING.md).

Конструктивная критика и доказанные контрпримеры считаются материалом для следующих версий.
