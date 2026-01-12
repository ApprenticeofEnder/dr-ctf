{config, ...}: {
  env = {
    FRONTEND_PORT = 5100;
    SERVICE_NAME = "dr-ctf-frontend";
  };

  # https://devenv.sh/languages/
  languages = {
    javascript = {
      enable = true;
      pnpm = {
        enable = true;
        install.enable = true;
      };
    };
    typescript.enable = true;
  };

  git-hooks.hooks = {
    prettier = {
      enable = true;
      language = "node";
      raw = {
        additional_dependencies = [
          "prettier-plugin-svelte"
          "prettier-plugin-tailwindcss"
        ];
      };
      settings = {
        binPath = "${config.devenv.root}/node_modules/.bin/prettier";
      };
    };
    eslint.enable = true;
  };
}
