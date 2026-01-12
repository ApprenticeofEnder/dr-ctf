{...}: {
  env = {
    FRONTEND_PORT = 5100;
    SERVICE_NAME = "dr-ctf-frontend";
  };

  # https://devenv.sh/languages/
  languages = {
    javascript = {
      enable = true;
      pnpm.enable = true;
    };
    typescript.enable = true;
  };

  git-hooks.hooks = {
    prettier.enable = true;
    eslint.enable = true;
  };
}
