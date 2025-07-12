<template>
  <div class="contact-container">
    <div class="contact-content">
      <h1 class="contact-title">Contáctanos</h1>
      
      <div class="contact-grid">
        <div class="contact-info">
          <h2>Información de Contacto</h2>
          
          <div class="contact-item">
            <div class="contact-icon">📍</div>
            <div>
              <h3>Dirección</h3>
              <p>Av. Principal 123<br>Ciudad, Estado 12345</p>
            </div>
          </div>
          
          <div class="contact-item">
            <div class="contact-icon">📞</div>
            <div>
              <h3>Teléfono</h3>
              <p>+1 (555) 123-4567</p>
            </div>
          </div>
          
          <div class="contact-item">
            <div class="contact-icon">✉️</div>
            <div>
              <h3>Email</h3>
              <p>info@clynera.com</p>
            </div>
          </div>
          
          <div class="contact-item">
            <div class="contact-icon">🕒</div>
            <div>
              <h3>Horarios</h3>
              <p>Lunes - Viernes: 7:00 AM - 6:00 PM<br>Sábados: 8:00 AM - 2:00 PM</p>
            </div>
          </div>
        </div>
        
        <div class="contact-form">
          <h2>Envíanos un Mensaje</h2>
          <form @submit.prevent="enviarMensaje">
            <div class="form-group">
              <label>Nombre Completo</label>
              <input type="text" v-model="formData.nombre" required />
            </div>
            
            <div class="form-group">
              <label>Email</label>
              <input type="email" v-model="formData.email" required />
            </div>
            
            <div class="form-group">
              <label>Asunto</label>
              <input type="text" v-model="formData.asunto" required />
            </div>
            
            <div class="form-group">
              <label>Mensaje</label>
              <textarea v-model="formData.mensaje" rows="5" required></textarea>
            </div>
            
            <button type="submit" :disabled="loading">
              {{ loading ? 'Enviando...' : 'Enviar Mensaje' }}
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const formData = ref({
  nombre: '',
  email: '',
  asunto: '',
  mensaje: ''
})

const loading = ref(false)

const enviarMensaje = () => {
  loading.value = true
  
  // Simular envío de mensaje
  setTimeout(() => {
    alert('Mensaje enviado correctamente. Nos pondremos en contacto contigo pronto.')
    formData.value = { nombre: '', email: '', asunto: '', mensaje: '' }
    loading.value = false
  }, 1000)
}
</script>

<style scoped>
.contact-container {
  min-height: 100vh;
  background: #f7f9fb;
  padding: 40px 20px;
}

.contact-content {
  max-width: 1200px;
  margin: 0 auto;
}

.contact-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 40px;
  color: #222;
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  margin-top: 40px;
}

.contact-info h2,
.contact-form h2 {
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 30px;
  color: #222;
}

.contact-item {
  display: flex;
  align-items: flex-start;
  margin-bottom: 30px;
  gap: 20px;
}

.contact-icon {
  font-size: 2rem;
  min-width: 40px;
}

.contact-item h3 {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 8px;
  color: #222;
}

.contact-item p {
  color: #666;
  line-height: 1.6;
}

.contact-form {
  background: #fff;
  border-radius: 16px;
  padding: 40px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.04);
}

.form-group {
  margin-bottom: 24px;
}

.form-group label {
  display: block;
  font-size: 1rem;
  font-weight: 500;
  margin-bottom: 8px;
  color: #222;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 12px 16px;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.2s;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #2196f3;
}

.form-group textarea {
  resize: vertical;
  min-height: 120px;
}

button {
  background: #2196f3;
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 12px 32px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
  width: 100%;
}

button:hover:not(:disabled) {
  background: #1769aa;
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

@media (max-width: 768px) {
  .contact-grid {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  
  .contact-title {
    font-size: 2rem;
  }
  
  .contact-form {
    padding: 30px 20px;
  }
}
</style> 