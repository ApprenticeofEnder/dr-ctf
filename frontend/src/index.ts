import { mount } from "svelte";
import App from "./App.svelte";
import "./index.css";

import { init } from "@svelte-router/core";

init();

const app = mount(App, {
  target: document.body,
  props: {
    name: "world",
  },
});

export default app;
