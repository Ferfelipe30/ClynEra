<template>
  <div class="services-container">
    <div class="services-content">
      <h1 class="services-title">Nuestros Servicios</h1>
      
      <div class="services-grid">
        <div class="service-card">
          <div class="service-icon">🩺</div>
          <h3>Análisis Clínicos</h3>
          <p>Realizamos todo tipo de análisis clínicos con la más alta precisión y tecnología avanzada.</p>
        </div>
        
        <div class="service-card">
          <div class="service-icon">🧬</div>
          <h3>Pruebas Especializadas</h3>
          <p>Pruebas genéticas y análisis especializados para diagnósticos precisos.</p>
        </div>
        
        <div class="service-card">
          <div class="service-icon">🔬</div>
          <h3>Microbiología</h3>
          <p>Análisis microbiológicos para detectar infecciones y enfermedades.</p>
        </div>
        
        <div class="service-card">
          <div class="service-icon">💊</div>
          <h3>Monitoreo Terapéutico</h3>
          <p>Seguimiento de niveles de medicamentos para optimizar tratamientos.</p>
        </div>
        
        <div class="service-card">
          <div class="service-icon">🩸</div>
          <h3>Hematología</h3>
          <p>Análisis completos de sangre y estudios hematológicos.</p>
        </div>
        
        <div class="service-card">
          <div class="service-icon">🧪</div>
          <h3>Química Clínica</h3>
          <p>Análisis bioquímicos para evaluar la función de órganos y sistemas.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.services-container {
  min-height: 100vh;
  background: #f7f9fb;
  padding: 40px 20px;
}

.services-content {
  max-width: 1200px;
  margin: 0 auto;
}

.services-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 40px;
  color: #222;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 30px;
  margin-top: 40px;
}

.service-card {
  background: #fff;
  border-radius: 16px;
  padding: 32px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.04);
  text-align: center;
  transition: transform 0.2s, box-shadow 0.2s;
}

.service-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 32px rgba(0,0,0,0.08);
}

.service-icon {
  font-size: 3rem;
  margin-bottom: 20px;
}

.service-card h3 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 16px;
  color: #222;
}

.service-card p {
  color: #666;
  line-height: 1.6;
  font-size: 1rem;
}

@media (max-width: 768px) {
  .services-grid {
    grid-template-columns: 1fr;
  }
  
  .services-title {
    font-size: 2rem;
  }
}
</style> 