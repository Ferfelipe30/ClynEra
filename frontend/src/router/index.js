import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PacienteRegistro from '../views/PacienteRegistro.vue'
import ListaPacientes from '../views/ListaPacientes.vue'
import OrdenRegistro from '../views/OrdenRegistro.vue'
import HistorialPaciente from '../views/HistorialPaciente.vue'
import DetalleOrden from '../views/DetalleOrden.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView, },
    { path: '/paciente', name: 'paciente', component: PacienteRegistro },
    { path: '/pacientes', name: 'lista-pacientes', component: ListaPacientes },
    { path: '/orden', name: 'orden', component: OrdenRegistro },
    { path: '/historial/:documento', name: 'historial', component: HistorialPaciente },
    { path: '/orden/detalle/:id', name: 'detalleOrden', component: DetalleOrden },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/services',
      name: 'services',
      component: () => import('../views/ServicesView.vue'),
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import('../views/ContactView.vue'),
    },
  ],
})

export default router
