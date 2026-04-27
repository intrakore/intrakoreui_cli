APP_VUE_BOILERPLATE = """<template>
  <div class="min-h-screen" :style="{ backgroundColor: 'var(--surface-gray-1)' }">
    <!-- Navigation Bar -->
    <div class="border-b" :style="{ backgroundColor: 'var(--surface-white)', borderColor: 'var(--outline-gray-1)' }">
      <div class="px-6 py-4 flex justify-between items-center">
        <h1 class="text-xl font-semibold" :style="{ color: 'var(--ink-blueprint-4)' }">
          Intrakore CRM
        </h1>
        <Button 
          v-if="$auth.isLoggedIn" 
          @click="$auth.logout()"
          variant="ghost"
          size="sm"
        >
          <template #prefix>
            <FeatherIcon name="log-out" class="w-4 h-4" />
          </template>
          Logout
        </Button>
      </div>
    </div>
    
    <!-- Main Content -->
    <div class="p-6">
      <router-view />
    </div>
  </div>
</template>

<script>
import { Button, FeatherIcon } from 'intrakore-ui'

export default {
  components: { Button, FeatherIcon },
  inject: ['$auth']
};
</script>
"""

HOME_VUE_BOILERPLATE = """<template>
  <div class="max-w-7xl mx-auto">
    <!-- Welcome Section -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold" :style="{ color: 'var(--ink-gray-9)' }">Home Page</h1>
      <p class="mt-2" :style="{ color: 'var(--ink-gray-5)' }">Welcome to your Intrakore dashboard</p>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
      <Card>
        <div class="p-4">
          <div class="flex items-center justify-between mb-2">
            <div class="text-sm" :style="{ color: 'var(--ink-gray-5)' }">Total Leads</div>
            <FeatherIcon name="users" class="w-4 h-4" :style="{ color: 'var(--ink-gray-4)' }" />
          </div>
          <div class="text-2xl font-bold" :style="{ color: 'var(--ink-gray-9)' }">0</div>
          <Badge theme="success" size="sm" class="mt-2">+12% this month</Badge>
        </div>
      </Card>
      
      <Card>
        <div class="p-4">
          <div class="flex items-center justify-between mb-2">
            <div class="text-sm" :style="{ color: 'var(--ink-gray-5)' }">Active Deals</div>
            <FeatherIcon name="briefcase" class="w-4 h-4" :style="{ color: 'var(--ink-gray-4)' }" />
          </div>
          <div class="text-2xl font-bold" :style="{ color: 'var(--ink-gray-9)' }">0</div>
          <Progress :value="65" size="sm" class="mt-2" />
        </div>
      </Card>
      
      <Card>
        <div class="p-4">
          <div class="flex items-center justify-between mb-2">
            <div class="text-sm" :style="{ color: 'var(--ink-gray-5)' }">Tasks Due</div>
            <FeatherIcon name="check-square" class="w-4 h-4" :style="{ color: 'var(--ink-gray-4)' }" />
          </div>
          <div class="text-2xl font-bold" :style="{ color: 'var(--ink-gray-9)' }">0</div>
        </div>
      </Card>
      
      <Card>
        <div class="p-4">
          <div class="flex items-center justify-between mb-2">
            <div class="text-sm" :style="{ color: 'var(--ink-gray-5)' }">Conversion Rate</div>
            <FeatherIcon name="trending-up" class="w-4 h-4" :style="{ color: 'var(--ink-gray-4)' }" />
          </div>
          <div class="text-2xl font-bold" :style="{ color: 'var(--ink-gray-9)' }">0%</div>
          <Rating :value="0" :max="5" size="sm" class="mt-2" />
        </div>
      </Card>
    </div>

    <!-- Connection Test Section -->
    <Card class="mb-8">
      <div class="p-6">
        <h3 class="text-lg font-medium mb-2" :style="{ color: 'var(--ink-gray-8)' }">Test Backend Connection</h3>
        <p class="mb-4" :style="{ color: 'var(--ink-gray-5)' }">Click the button to test connection to your Frappe backend.</p>
        
        <Button 
          @click="$resources.ping.fetch()"
          :loading="$resources.ping.loading"
          variant="solid"
          theme="primary"
        >
          <template #prefix>
            <FeatherIcon name="activity" class="w-4 h-4" />
          </template>
          {{ $resources.ping.loading ? 'Connecting...' : 'Test Connection' }}
        </Button>

        <div v-if="$resources.ping.data" class="mt-4">
          <Alert title="Connected Successfully" theme="success" closable>
            Server response: {{ $resources.ping.data }}
          </Alert>
        </div>

        <div v-if="$resources.ping.error" class="mt-4">
          <Alert title="Connection Failed" theme="error" closable>
            {{ $resources.ping.error }}
          </Alert>
        </div>
      </div>
    </Card>

    <!-- Quick Actions -->
    <Card>
      <div class="p-6">
        <h3 class="text-lg font-medium mb-4" :style="{ color: 'var(--ink-gray-8)' }">Quick Actions</h3>
        <div class="flex flex-wrap gap-3">
          <Button variant="outline">
            <template #prefix>
              <FeatherIcon name="user-plus" class="w-4 h-4" />
            </template>
            Add Lead
          </Button>
          <Button variant="outline">
            <template #prefix>
              <FeatherIcon name="file-text" class="w-4 h-4" />
            </template>
            Generate Report
          </Button>
          <Button variant="outline">
            <template #prefix>
              <FeatherIcon name="settings" class="w-4 h-4" />
            </template>
            Settings
          </Button>
        </div>
      </div>
    </Card>
  </div>
</template>

<script>
import { 
  Card, 
  Button, 
  Alert, 
  Badge, 
  Progress,
  Rating,
  FeatherIcon
} from 'intrakore-ui'

export default {
  name: 'HomePage',
  components: {
    Card,
    Button,
    Alert,
    Badge,
    Progress,
    Rating,
    FeatherIcon
  },
  resources: {
    ping() {
      return {
        method: "frappe.ping",
        onSuccess(data) {
          console.log("Ping successful:", data);
        },
        onError(error) {
          console.error("Ping failed:", error);
        },
      };
    },
  },
};
</script>
"""

LOGIN_VUE_BOILERPLATE = """<template>
  <div class="min-h-screen flex items-center justify-center" :style="{ backgroundColor: 'var(--surface-gray-1)' }">
    <Card class="w-full max-w-md">
      <div class="p-8">
        <div class="text-center mb-8">
          <h2 class="text-2xl font-bold" :style="{ color: 'var(--ink-gray-9)' }">Welcome Back</h2>
          <p class="mt-2" :style="{ color: 'var(--ink-gray-5)' }">Sign in to your account</p>
        </div>

        <form @submit.prevent="login" class="space-y-6">
          <div>
            <FormLabel label="Username" required />
            <TextInput 
              v-model="email" 
              placeholder="Enter your username"
              size="md"
              block
            />
          </div>

          <div>
            <FormLabel label="Password" required />
            <TextInput 
              v-model="password" 
              type="password"
              placeholder="Enter your password"
              size="md"
              block
            />
          </div>

          <Button 
            type="submit"
            variant="solid"
            theme="primary"
            block
            :loading="loading"
          >
            <template #prefix>
              <FeatherIcon name="log-in" class="w-4 h-4" />
            </template>
            Sign In
          </Button>
        </form>

        <div v-if="errorMessage" class="mt-4">
          <Alert theme="error" size="sm">
            {{ errorMessage }}
          </Alert>
        </div>
      </div>
    </Card>
  </div>
</template>

<script>
import { Card, Button, FormLabel, TextInput, Alert, FeatherIcon } from 'intrakore-ui'

export default {
  name: 'LoginPage',
  components: {
    Card,
    Button,
    FormLabel,
    TextInput,
    Alert,
    FeatherIcon
  },
  data() {
    return {
      email: null,
      password: null,
      loading: false,
      errorMessage: null,
      redirect_route: null
    };
  },
  inject: ["$auth"],
  async mounted() {
    if (this.$route?.query?.route) {
      this.redirect_route = this.$route.query.route;
      this.$router.replace({ query: null });
    }
  },
  methods: {
    async login() {
      if (!this.email || !this.password) {
        this.errorMessage = 'Please enter username and password';
        return;
      }
      
      this.loading = true;
      this.errorMessage = null;
      
      try {
        let res = await this.$auth.login(this.email, this.password);
        if (res) {
          this.$router.push({ name: "Home" });
        } else {
          this.errorMessage = 'Invalid username or password';
        }
      } catch (error) {
        this.errorMessage = error.message || 'Login failed';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
"""

VUE_VITE_CONFIG_BOILERPLATE = """import path from 'path';
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import intrakoreui from 'intrakore-ui/vite';

export default defineConfig({
  plugins: [
    intrakoreui({
      frappeProxy: true,
      jinjaBootData: true,
      lucideIcons: true,
      buildConfig: {
        outDir: '../{{app}}/public/{{name}}',
        indexHtmlPath: '../{{app}}/www/{{name}}.html',
        emptyOutDir: true,
        sourcemap: true,
      },
    }),
    vue(),
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  build: {
    outDir: '../{{app}}/public/{{name}}',
    emptyOutDir: true,
    target: 'es2015',
  },
  optimizeDeps: {
    include: ['intrakore-ui > feather-icons', 'showdown', 'engine.io-client', 'lucide-vue-next'],
  },
});
"""

PROXY_OPTIONS_BOILERPLATE = """const common_site_config = require('../../../sites/common_site_config.json');
const { webserver_port } = common_site_config;

export default {
	'^/(app|api|assets|files|private)': {
		target: `http://127.0.0.1:${webserver_port}`,
		ws: true,
		router: function(req) {
			const site_name = req.headers.host.split(':')[0];
			return `http://${site_name}:${webserver_port}`;
		}
	}
};
"""

MAIN_JS_BOILERPLATE = """import { createApp, reactive } from "vue";
import App from "./App.vue";
import 'intrakore-ui/tokens.css';

import router from './router';
import resourceManager from "../../../intrakoreui_cli/libs/resourceManager";
import call from "../../../intrakoreui_cli/libs/controllers/call";
import socket from "../../../intrakoreui_cli/libs/controllers/socket";
import Auth from "../../../intrakoreui_cli/libs/controllers/auth";

const app = createApp(App);
const auth = reactive(new Auth());

// Plugins
app.use(router);
app.use(resourceManager);

// Global Properties,
// components can inject this
app.provide("$auth", auth);
app.provide("$call", call);
app.provide("$socket", socket);


// Configure route guards
router.beforeEach(async (to, from, next) => {
	if (to.matched.some((record) => !record.meta.isLoginPage)) {
		// this route requires auth, check if logged in
		// if not, redirect to login page.
		if (!auth.isLoggedIn) {
			next({ name: 'Login', query: { route: to.path } });
		} else {
			next();
		}
	} else {
		if (auth.isLoggedIn) {
			next({ name: 'Home' });
		} else {
			next();
		}
	}
});

app.mount("#app");
"""

ROUTER_INDEX_BOILERPLATE = """import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import authRoutes from './auth';

const routes = [
  {
	path: "/",
	name: "Home",
	component: Home,
  },
  ...authRoutes,
];

const router = createRouter({
  history: createWebHistory("/{{name}}"),
  routes,
});

export default router;
"""


AUTH_ROUTES_BOILERPLATE = """export default [
	{
		path: '/login',
		name: 'Login',
		component: () =>
			import(/* webpackChunkName: "login" */ '../views/Login.vue'),
		meta: {
			isLoginPage: true
		},
		props: true
	}
]
"""

REACT_VITE_CONFIG_BOILERPLATE = """import path from 'path';
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import intrakoreui from 'intrakore-ui/vite';

export default defineConfig({
  plugins: [
    intrakoreui({
      frappeProxy: true,
      jinjaBootData: true,
      lucideIcons: true,
      buildConfig: {
        outDir: '../{{app}}/public/{{name}}',
        indexHtmlPath: '../{{app}}/www/{{name}}.html',
        emptyOutDir: true,
        sourcemap: true,
      },
    }),
    react(),
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  build: {
    outDir: '../{{app}}/public/{{name}}',
    emptyOutDir: true,
    target: 'es2015',
  },
  optimizeDeps: {
    include: ['intrakore-ui > feather-icons', 'showdown', 'engine.io-client', 'lucide-react'],
  },
});
"""

APP_REACT_BOILERPLATE = """import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import { FrappeProvider } from 'frappe-react-sdk'
function App() {
  const [count, setCount] = useState(0)

  return (
	<div className="App">
	  <FrappeProvider>
		<div>
	  <div>
		<a href="https://vitejs.dev" target="_blank">
		  <img src="/vite.svg" className="logo" alt="Vite logo" />
		</a>
		<a href="https://reactjs.org" target="_blank">
		  <img src={reactLogo} className="logo react" alt="React logo" />
		</a>
	  </div>
	  <h1>Vite + React + Frappe</h1>
	  <div className="card">
		<button onClick={() => setCount((count) => count + 1)}>
		  count is {count}
		</button>
		<p>
		  Edit <code>src/App.jsx</code> and save to test HMR
		</p>
	  </div>
	  <p className="read-the-docs">
		Click on the Vite and React logos to learn more
	  </p>
	  </div>
	  </FrappeProvider>
	</div>
  )
}

export default App
"""

DESK_PAGE_JS_TEMPLATE = """frappe.pages["{{ page_name }}"].on_page_load = function (wrapper) {
	frappe.ui.make_app_page({
		parent: wrapper,
		title: __("{{ page_title }}"),
		single_column: true,
	});
};

frappe.pages["{{ page_name }}"].on_page_show = function (wrapper) {
	load_desk_page(wrapper);
};

function load_desk_page(wrapper) {
	let $parent = $(wrapper).find(".layout-main-section");
	$parent.empty();

	frappe.require("{{ scrubbed_name }}.bundle.{{ bundle_type }}").then(() => {
		frappe.{{ scrubbed_name }} = new frappe.ui.{{ pascal_cased_name }}({
			wrapper: $parent,
			page: wrapper.page,
		});
	});
}
"""

DESK_PAGE_JS_BUNDLE_TEMPLATE_VUE = """import { createApp } from "vue";
import App from "./App.vue";


class {{ pascal_cased_name }} {
	constructor({ page, wrapper }) {
		this.$wrapper = $(wrapper);
		this.page = page;

		this.init();
	}

	init() {
		this.setup_page_actions();
		this.setup_app();
	}

	setup_page_actions() {
		// setup page actions
		this.primary_btn = this.page.set_primary_action(__("Print Message"), () =>
	  frappe.msgprint("Hello My Page!")
		);
	}

	setup_app() {
		// create a vue instance
		let app = createApp(App);
		// mount the app
		this.${{ scrubbed_name }} = app.mount(this.$wrapper.get(0));
	}
}

frappe.provide("frappe.ui");
frappe.ui.{{ pascal_cased_name }} = {{ pascal_cased_name }};
export default {{ pascal_cased_name }};
"""

DESK_PAGE_VUE_APP_COMPONENT_BOILERPLATE = """<script setup>
import { ref } from "vue";

const dynamicMessage = ref("Hello from App.vue");
</script>
<template>
  <div>
	<h3>{{ dynamicMessage }}</h3>
    <h4>Start editing at {{ app_component_path }}</h4>
  </div>
</template>"""

DESK_PAGE_REACT_APP_COMPONENT_BOILERPLATE = """import * as React from "react";

export function App() {
  const dynamicMessage = React.useState("Hello from App.jsx");
  return (
    <div className="m-4">
      <h3>{dynamicMessage}</h3>
      <h4>Start editing at {{ app_component_path }}</h4>
    </div>
  );
}"""

DESK_PAGE_JSX_BUNDLE_TEMPLATE_REACT = """import * as React from "react";
import { App } from "./App";
import { createRoot } from "react-dom/client";


class {{ pascal_cased_name }} {
	constructor({ page, wrapper }) {
		this.$wrapper = $(wrapper);
		this.page = page;

		this.init();
	}

	init() {
		this.setup_page_actions();
		this.setup_app();
	}

	setup_page_actions() {
		// setup page actions
		this.primary_btn = this.page.set_primary_action(__("Print Message"), () =>
	  		frappe.msgprint("Hello My Page!")
		);
	}

	setup_app() {
		// create and mount the react app
		const root = createRoot(this.$wrapper.get(0));
		root.render(<App />);
		this.${{ scrubbed_name }} = root;
	}
}

frappe.provide("frappe.ui");
frappe.ui.{{ pascal_cased_name }} = {{ pascal_cased_name }};
export default {{ pascal_cased_name }};
"""


HTML_CONTEXT_PY_BOILERPLATE = """import frappe
from frappe.utils import get_system_timezone

no_cache = 1


def get_context():
	csrf_token = frappe.sessions.get_csrf_token()
	context = frappe._dict()
	context.boot = get_boot()
	context.boot.csrf_token = csrf_token
	return context


@frappe.whitelist(methods=["POST"], allow_guest=True)
def get_context_for_dev():
	if not frappe.conf.developer_mode:
		frappe.throw("This method is only meant for developer mode")
	return get_boot()


def get_boot():
	return frappe._dict(
		{
			"frappe_version": frappe.__version__,
			"site_name": frappe.local.site,
			"read_only_mode": frappe.flags.read_only,
			"system_timezone": get_system_timezone(),
		}
	)
"""