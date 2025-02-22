## ts-playwright

Test by typing:

```bash
pnpm exec playwright test
```

Check out the following files:

- `./tests/example.spec.ts` - Example end-to-end test
- `./tests-examples/demo-todo-app.spec.ts` - Demo Todo App end-to-end tests
- `./playwright.config.ts` - Playwright Test configuration

Visit https://playwright.dev/docs/intro for more information. ✨

Other important commands:

```bash
pnpm exec playwright test
# Runs the end-to-end tests.

pnpm exec playwright test --ui
# Starts the interactive UI mode.

pnpm exec playwright test --project=chromium
# Runs the tests only on Desktop Chrome.

pnpm exec playwright test example
# Runs the tests in a specific file.

pnpm exec playwright test --debug
# Runs the tests in debug mode.

pnpm exec playwright codegen
# Auto generate tests with Codegen.
```

Happy hacking! 🎭
