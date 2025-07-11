<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

const mobileMenuOpen = ref(false)
const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}
</script>

<template>
  <nav class="main-navbar">
    <div class="navbar-left">
      <RouterLink to="/" class="navbar-logo">
        <span class="logo-icon">✚</span>
        <span class="logo-text">ClynEra</span>
      </RouterLink>
    </div>
    <button class="navbar-burger" @click="toggleMobileMenu" aria-label="Open menu" :aria-expanded="mobileMenuOpen">
      <span></span><span></span><span></span>
    </button>
    <div :class="['navbar-center', { open: mobileMenuOpen }]">
      <RouterLink to="/services" class="navbar-link" @click="mobileMenuOpen = false">Services</RouterLink>
      <RouterLink to="/about" class="navbar-link" @click="mobileMenuOpen = false">About Us</RouterLink>
      <RouterLink to="/historial/:documento" class="navbar-link" @click="mobileMenuOpen = false">Historial Paciente</RouterLink>
      <RouterLink to="/contact" class="navbar-link" @click="mobileMenuOpen = false">Contact</RouterLink>
      <div class="navbar-right">
        <RouterLink to="/paciente" class="btn btn-primary" @click="mobileMenuOpen = false">New Patient Registration</RouterLink>
        <RouterLink to="/orden" class="btn btn-secondary" @click="mobileMenuOpen = false">Orden de Examen</RouterLink>
      </div>
    </div>
  </nav>
  <main class="main-content">
    <RouterView />
  </main>
</template>

<style scoped>
.main-navbar {
  width: 100%;
  background: #fff;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
  height: 64px;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 8px rgba(0,0,0,0.02);
}
.main-content {
  width: 100vw;
  min-height: 100vh;
  background: #fff;
  display: block;
  padding: 0;
  margin: 0;
}
.navbar-left {
  display: flex;
  align-items: center;
}
.navbar-logo {
  display: flex;
  align-items: center;
  font-weight: 700;
  font-size: 1.3rem;
  color: #222;
  text-decoration: none;
  gap: 8px;
}
.logo-icon {
  font-size: 1.5rem;
  color: #2196f3;
}
.logo-text {
  letter-spacing: 0.5px;
}
.navbar-burger {
  display: none;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 40px;
  height: 40px;
  background: none;
  border: none;
  cursor: pointer;
  margin-left: 12px;
}
.navbar-burger span {
  display: block;
  width: 24px;
  height: 3px;
  background: #222;
  margin: 3px 0;
  border-radius: 2px;
  transition: all 0.3s;
}
.navbar-center {
  display: flex;
  align-items: center;
  gap: 32px;
  transition: max-height 0.3s;
}
.navbar-link {
  color: #222;
  text-decoration: none;
  font-weight: 500;
  font-size: 1rem;
  transition: color 0.2s;
  padding: 6px 0;
  position: relative;
  outline: none;
}
.navbar-link.router-link-exact-active,
.navbar-link:focus,
.navbar-link:hover {
  color: #2196f3;
  text-decoration: underline;
}
.navbar-right {
  display: flex;
  gap: 12px;
}
.btn {
  display: inline-block;
  padding: 8px 18px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  text-decoration: none;
  border: none;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;
  outline: none;
}
.btn:focus {
  box-shadow: 0 0 0 2px #2196f3;
}
.btn-primary {
  background: #2196f3;
  color: #fff;
}
.btn-primary:hover,
.btn-primary:focus {
  background: #1769aa;
}
.btn-secondary {
  background: #f3f4f6;
  color: #222;
  border: 1px solid #e5e7eb;
}
.btn-secondary:hover,
.btn-secondary:focus {
  background: #e5e7eb;
}
@media (max-width: 900px) {
  .main-navbar {
    flex-wrap: wrap;
    padding: 0 8px;
    height: auto;
    min-height: 56px;
  }
  .navbar-burger {
    display: flex;
  }
  .navbar-center {
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
    background: #fff;
    position: absolute;
    left: 0;
    top: 64px;
    max-height: 0;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    border-bottom-left-radius: 8px;
    border-bottom-right-radius: 8px;
    z-index: 99;
    padding: 0 16px;
    gap: 0;
    transition: max-height 0.3s;
  }
  .navbar-center.open {
    max-height: 400px;
    padding: 16px 16px 12px 16px;
    gap: 18px;
  }
  .navbar-link {
    padding: 10px 0;
    width: 100%;
    font-size: 1.1rem;
  }
  .navbar-right {
    flex-direction: column;
    gap: 10px;
    width: 100%;
    margin-top: 8px;
  }
  .main-content {
    padding: 0;
  }
}
@media (max-width: 600px) {
  .main-navbar {
    padding: 0 2px;
  }
  .navbar-logo {
    font-size: 1.1rem;
  }
  .btn {
    font-size: 0.95rem;
    padding: 8px 10px;
  }
  .main-content {
    padding: 0;
  }
}
</style>
