# React Boilerplates (Add these to your file)
INDEX_CSS_BOILERPLATE_REACT = """/* === Intrakore UI Design Tokens === */
:root {
  --outline-white: #F9F9F9;
  --outline-gray-1: #D5D5E2;
  --outline-gray-2: #BDBDD1;
  --outline-gray-3: #9F9FBC;
  --outline-gray-4: #8181A7;
  --outline-gray-5: #36364E;
  --outline-blueprint-1: #B9BEFE;
  --outline-blueprint-2: #8D95F6;
  --outline-blueprint-3: #5763FA;
  --outline-blueprint-4: #000FCC;
  --outline-dusk-1: #CAC3FE;
  --outline-dusk-2: #A194F9;
  --outline-dusk-3: #705CFF;
  --outline-dusk-4: #3E25D0;
  --outline-clearing-1: #A9E5D0;
  --outline-clearing-2: #68C2A3;
  --outline-red-1: #FFD8D8;
  --outline-red-2: #FDC2C2;
  --outline-red-3: #F79596;
  --outline-red-4: #E03636;
  --outline-green-1: #B9EECC;
  --outline-green-2: #9BE4B6;
  --outline-amber-1: #FEEDA9;
  --outline-amber-2: #FBCC55;
  --outline-blue-1: #A7D7FD;
  --outline-blue-2: #0289F7;
  --outline-gray-modals: #D5D5E2;
  --outline-orange-1: #F4B07F;
  --surface-white: #F9F9F9;
  --surface-gray-1: #F3F3F7;
  --surface-gray-2: #E8E8EF;
  --surface-gray-3: #D5D5E2;
  --surface-gray-4: #BDBDD1;
  --surface-gray-5: #4B4B6C;
  --surface-gray-6: #36364E;
  --surface-gray-7: #212130;
  --surface-blueprint-1: #EBECFF;
  --surface-blueprint-2: #D6D9FF;
  --surface-blueprint-3: #B9BEFE;
  --surface-blueprint-4: #8D95F6;
  --surface-blueprint-5: #2A37F4;
  --surface-blueprint-6: #0717E4;
  --surface-blueprint-7: #000FCC;
  --surface-blueprint-8: #0310AA;
  --surface-blueprint-9: #050D76;
  --surface-dusk-1: #DBD6FF;
  --surface-dusk-2: #CAC3FE;
  --surface-dusk-3: #A194F9;
  --surface-dusk-4: #705CFF;
  --surface-dusk-5: #533EEA;
  --surface-dusk-6: #3E25D0;
  --surface-clearing-1: #EFFBF7;
  --surface-clearing-2: #DDF8EF;
  --surface-clearing-3: #68C2A3;
  --surface-red-1: #FFE7E7;
  --surface-red-2: #FFD8D8;
  --surface-red-3: #FDC2C2;
  --surface-red-4: #CC2929;
  --surface-red-5: #B52A2A;
  --surface-red-6: #941F1F;
  --surface-green-1: #F2FDF4;
  --surface-green-2: #E4FAEB;
  --surface-green-3: #30A66D;
  --surface-amber-1: #FFF7D3;
  --surface-amber-2: #DB7706;
  --surface-orange-1: #FFEFE4;
  --surface-blue-1: #E6F4FF;
  --surface-blue-2: #0289F7;
  --surface-violet-1: #D6D9FF;
  --surface-cyan-1: #DDF7FF;
  --surface-pink-1: #FDE8F5;
  --surface-modal: #F9F9F9;
  --surface-cards: #F9F9F9;
  --surface-menu-bar: #050D76;
  --surface-selected: #000FCC;
  --ink-white: #F9F9F9;
  --ink-gray-1: #D5D5E2;
  --ink-gray-2: #BDBDD1;
  --ink-gray-3: #9F9FBC;
  --ink-gray-4: #8181A7;
  --ink-gray-5: #60608A;
  --ink-gray-6: #4B4B6C;
  --ink-gray-7: #4B4B6C;
  --ink-gray-8: #36364E;
  --ink-gray-9: #212130;
  --ink-blueprint-1: #EBECFF;
  --ink-blueprint-2: #5763FA;
  --ink-blueprint-3: #2A37F4;
  --ink-blueprint-4: #000FCC;
  --ink-dusk-1: #EDEBFF;
  --ink-dusk-2: #705CFF;
  --ink-dusk-3: #533EEA;
  --ink-dusk-4: #3E25D0;
  --ink-clearing-1: #EFFBF7;
  --ink-clearing-2: #36BF8F;
  --ink-clearing-3: #149064;
  --ink-red-1: #FFF7F7;
  --ink-red-2: #F79596;
  --ink-red-3: #E03636;
  --ink-red-4: #CC2929;
  --ink-green-1: #F2FDF4;
  --ink-green-2: #30A66D;
  --ink-green-3: #16794C;
  --ink-amber-1: #FFF7D3;
  --ink-amber-2: #E79913;
  --ink-amber-3: #DB7706;
  --ink-blue-1: #F2F8FF;
  --ink-blue-2: #0289F7;
  --ink-blue-3: #007BE0;
  --ink-cyan-1: #3BBDE5;
  --ink-pink-1: #E34AA6;
  --ink-violet-1: #2A37F4;
}

[data-theme="dark"] {
  --outline-white: #1C1C1C;
  --outline-gray-1: #232323;
  --outline-gray-2: #343434;
  --outline-gray-3: #424242;
  --outline-gray-4: #808080;
  --outline-gray-5: #D5D5E2;
  --outline-blueprint-1: #000B99;
  --outline-blueprint-2: #000FCC;
  --outline-blueprint-3: #0D1BF2;
  --outline-blueprint-4: #3947F9;
  --outline-dusk-1: #2C18B4;
  --outline-dusk-2: #3E25D0;
  --outline-dusk-3: #533EEA;
  --outline-dusk-4: #705CFF;
  --outline-clearing-1: #23A97A;
  --outline-clearing-2: #4AAF8E;
  --outline-red-1: #621B18;
  --outline-red-2: #4C1818;
  --outline-red-3: #621B18;
  --outline-red-4: #9C2020;
  --outline-green-1: #0B6139;
  --outline-green-2: #0A3F27;
  --outline-amber-1: #824108;
  --outline-amber-2: #824108;
  --outline-blue-1: #155999;
  --outline-blue-2: #155999;
  --outline-gray-modals: #343434;
  --outline-orange-1: #823906;
  --surface-white: #0F0F0F;
  --surface-gray-1: #232323;
  --surface-gray-2: #FFFFFF1A;
  --surface-gray-3: #FFFFFF2E;
  --surface-gray-4: #424242;
  --surface-gray-5: #D4D4D4;
  --surface-gray-6: #AFAFAF;
  --surface-gray-7: #D4D4D4;
  --surface-blueprint-1: #030740;
  --surface-blueprint-2: #020964;
  --surface-blueprint-3: #000B99;
  --surface-blueprint-4: #000FCC;
  --surface-blueprint-5: #3947F9;
  --surface-blueprint-6: #0D1BF2;
  --surface-blueprint-7: #000FCC;
  --surface-blueprint-8: #3947F9;
  --surface-blueprint-9: #707CFF;
  --surface-dusk-1: #15077E;
  --surface-dusk-2: #1F0F95;
  --surface-dusk-3: #2C18B4;
  --surface-dusk-4: #705CFF;
  --surface-dusk-5: #3E25D0;
  --surface-dusk-6: #2C18B4;
  --surface-clearing-1: #038255;
  --surface-clearing-2: #149064;
  --surface-clearing-3: #4AAF8E;
  --surface-red-1: #361515CC;
  --surface-red-2: #4C1818E6;
  --surface-red-3: #621B18;
  --surface-red-4: #E43838;
  --surface-red-5: #9C2020;
  --surface-red-6: #621B18;
  --surface-green-1: #0B2E1C;
  --surface-green-2: #0A3F27;
  --surface-green-3: #1F9D60;
  --surface-amber-1: #371E06;
  --surface-amber-2: #C57411;
  --surface-orange-1: #401F07CC;
  --surface-blue-1: #0E2037;
  --surface-blue-2: #1580D8;
  --surface-violet-1: #030740;
  --surface-cyan-1: #0B252D;
  --surface-pink-1: #471432CC;
  --surface-modal: #232323;
  --surface-cards: #1C1C1C;
  --surface-menu-bar: #030740;
  --surface-selected: #FFFFFF1A;
  --ink-white: #000B99;
  --ink-gray-1: #232323;
  --ink-gray-2: #424242;
  --ink-gray-3: #717171;
  --ink-gray-4: #717171;
  --ink-gray-5: #808080;
  --ink-gray-6: #999999;
  --ink-gray-7: #AFAFAF;
  --ink-gray-8: #D4D4D4;
  --ink-gray-9: #F8F8F8;
  --ink-blueprint-1: #F9F9F9;
  --ink-blueprint-2: #C2C7FF;
  --ink-blueprint-3: #99A2FF;
  --ink-blueprint-4: #C2C7FF;
  --ink-dusk-1: #F9F9F9;
  --ink-dusk-2: #2C18B4;
  --ink-dusk-3: #9A8FFF;
  --ink-dusk-4: #B8AFFF;
  --ink-clearing-1: #F9F9F9;
  --ink-clearing-2: #68C2A3;
  --ink-clearing-3: #96E4CC;
  --ink-red-1: #F9F9F9;
  --ink-red-2: #621B18;
  --ink-red-3: #EB4D52;
  --ink-red-4: #FC7474;
  --ink-green-1: #F9F9F9;
  --ink-green-2: #35AE74;
  --ink-green-3: #78D7A9;
  --ink-amber-1: #F9F9F9;
  --ink-amber-2: #E79913;
  --ink-amber-3: #E79913;
  --ink-blue-1: #F9F9F9;
  --ink-blue-2: #5AAEF2;
  --ink-blue-3: #8CC1EC;
  --ink-cyan-1: #3CB8DC;
  --ink-pink-1: #E359AB;
  --ink-violet-1: #707CFF;
}

/* === Tailwind Directives === */
@tailwind base;
@tailwind components;
@tailwind utilities;
"""

APP_REACT_BOILERPLATE_FULL = """import { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';
import { IntrakoreProvider, useAuth } from 'intrakore-ui';
import Home from './views/Home';
import Login from './views/Login';
import './index.css';

function AppContent() {
  const { isLoggedIn, logout } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (!isLoggedIn) {
      navigate('/login');
    }
  }, [isLoggedIn, navigate]);

  return (
    <div className="min-h-screen" style={{ backgroundColor: 'var(--surface-gray-1)' }}>
      <div className="border-b" style={{ backgroundColor: 'var(--surface-white)', borderColor: 'var(--outline-gray-1)' }}>
        <div className="px-6 py-4 flex justify-between items-center">
          <h1 className="text-xl font-semibold" style={{ color: 'var(--ink-blueprint-4)' }}>
            Intrakore App
          </h1>
          {isLoggedIn && (
            <button
              onClick={logout}
              className="px-3 py-1 text-sm rounded hover:bg-gray-100"
              style={{ color: 'var(--ink-gray-6)' }}
            >
              Logout
            </button>
          )}
        </div>
      </div>
      <div className="p-6">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
    </div>
  );
}

function App() {
  return (
    <IntrakoreProvider>
      <Router>
        <AppContent />
      </Router>
    </IntrakoreProvider>
  );
}

export default App;
"""

HOME_REACT_BOILERPLATE = """import { useState } from 'react';
import { Card, Button, Alert, Badge, Progress, Rating, FeatherIcon, useFrappeCall } from 'intrakore-ui';

export default function Home() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const testConnection = async () => {
    setLoading(true);
    setResult(null);
    try {
      const response = await fetch('/api/method/frappe.ping', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
      const data = await response.json();
      setResult({ success: true, message: data.message || 'Connected successfully!' });
    } catch (error) {
      setResult({ success: false, message: error.message });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-7xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-bold" style={{ color: 'var(--ink-gray-9)' }}>Home Page</h1>
        <p className="mt-2" style={{ color: 'var(--ink-gray-5)' }}>Welcome to your Intrakore dashboard</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <Card>
          <div className="p-4">
            <div className="flex items-center justify-between mb-2">
              <div className="text-sm" style={{ color: 'var(--ink-gray-5)' }}>Total Leads</div>
              <FeatherIcon name="users" className="w-4 h-4" style={{ color: 'var(--ink-gray-4)' }} />
            </div>
            <div className="text-2xl font-bold" style={{ color: 'var(--ink-gray-9)' }}>0</div>
            <Badge theme="success" size="sm" className="mt-2">+12% this month</Badge>
          </div>
        </Card>
        <Card>
          <div className="p-4">
            <div className="flex items-center justify-between mb-2">
              <div className="text-sm" style={{ color: 'var(--ink-gray-5)' }}>Active Deals</div>
              <FeatherIcon name="briefcase" className="w-4 h-4" style={{ color: 'var(--ink-gray-4)' }} />
            </div>
            <div className="text-2xl font-bold" style={{ color: 'var(--ink-gray-9)' }}>0</div>
            <Progress value={65} size="sm" className="mt-2" />
          </div>
        </Card>
        <Card>
          <div className="p-4">
            <div className="flex items-center justify-between mb-2">
              <div className="text-sm" style={{ color: 'var(--ink-gray-5)' }}>Tasks Due</div>
              <FeatherIcon name="check-square" className="w-4 h-4" style={{ color: 'var(--ink-gray-4)' }} />
            </div>
            <div className="text-2xl font-bold" style={{ color: 'var(--ink-gray-9)' }}>0</div>
          </div>
        </Card>
        <Card>
          <div className="p-4">
            <div className="flex items-center justify-between mb-2">
              <div className="text-sm" style={{ color: 'var(--ink-gray-5)' }}>Conversion Rate</div>
              <FeatherIcon name="trending-up" className="w-4 h-4" style={{ color: 'var(--ink-gray-4)' }} />
            </div>
            <div className="text-2xl font-bold" style={{ color: 'var(--ink-gray-9)' }}>0%</div>
            <Rating value={0} max={5} size="sm" className="mt-2" />
          </div>
        </Card>
      </div>

      <Card className="mb-8">
        <div className="p-6">
          <h3 className="text-lg font-medium mb-2" style={{ color: 'var(--ink-gray-8)' }}>Test Backend Connection</h3>
          <p className="mb-4" style={{ color: 'var(--ink-gray-5)' }}>Click the button to test connection to your Frappe backend.</p>
          <Button onClick={testConnection} loading={loading} variant="solid" theme="primary">
            <FeatherIcon name="activity" className="w-4 h-4 mr-2" />
            {loading ? 'Connecting...' : 'Test Connection'}
          </Button>
          {result && (
            <div className="mt-4">
              <Alert title={result.success ? 'Connected Successfully' : 'Connection Failed'} theme={result.success ? 'success' : 'error'}>
                {result.message}
              </Alert>
            </div>
          )}
        </div>
      </Card>

      <Card>
        <div className="p-6">
          <h3 className="text-lg font-medium mb-4" style={{ color: 'var(--ink-gray-8)' }}>Quick Actions</h3>
          <div className="flex flex-wrap gap-3">
            <Button variant="outline"><FeatherIcon name="user-plus" className="w-4 h-4 mr-2" />Add Lead</Button>
            <Button variant="outline"><FeatherIcon name="file-text" className="w-4 h-4 mr-2" />Generate Report</Button>
            <Button variant="outline"><FeatherIcon name="settings" className="w-4 h-4 mr-2" />Settings</Button>
          </div>
        </div>
      </Card>
    </div>
  );
}
"""

LOGIN_REACT_BOILERPLATE = """import { useState } from 'react';
import { Card, Button, FormLabel, TextInput, Alert, FeatherIcon, useAuth } from 'intrakore-ui';
import { useNavigate } from 'react-router-dom';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!email || !password) {
      setError('Please enter username and password');
      return;
    }
    setLoading(true);
    setError(null);
    try {
      const success = await login(email, password);
      if (success) {
        navigate('/');
      } else {
        setError('Invalid username or password');
      }
    } catch (err) {
      setError(err.message || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center" style={{ backgroundColor: 'var(--surface-gray-1)' }}>
      <Card className="w-full max-w-md">
        <div className="p-8">
          <div className="text-center mb-8">
            <h2 className="text-2xl font-bold" style={{ color: 'var(--ink-gray-9)' }}>Welcome Back</h2>
            <p className="mt-2" style={{ color: 'var(--ink-gray-5)' }}>Sign in to your account</p>
          </div>
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <FormLabel label="Username" required />
              <TextInput value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Enter your username" size="md" block />
            </div>
            <div>
              <FormLabel label="Password" required />
              <TextInput type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Enter your password" size="md" block />
            </div>
            <Button type="submit" variant="solid" theme="primary" block loading={loading}>
              <FeatherIcon name="log-in" className="w-4 h-4 mr-2" />Sign In
            </Button>
          </form>
          {error && (
            <div className="mt-4">
              <Alert theme="error" size="sm">{error}</Alert>
            </div>
          )}
        </div>
      </Card>
    </div>
  );
}
"""

# Also add REACT_MAIN_JSX_BOILERPLATE for the entry point
REACT_MAIN_JSX_BOILERPLATE = """import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
"""

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