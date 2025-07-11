<script setup>
// Puedes agregar lógica de navegación si lo deseas
</script>

<template>
  <div class="home-landing-simple">
    <!-- Hero Section -->
    <section class="hero-section-simple">
      <div class="hero-content-simple">
        <h1>Precision Diagnostics for a Healthier Tomorrow</h1>
        <p>ClynEra provides accurate and timely diagnostic testing for healthcare providers and patients.</p>
        <button class="hero-btn-simple">Learn More</button>
      </div>
    </section>

    <!-- Services Section -->
    <section class="services-section-simple">
      <h2>Our Services</h2>
      <div class="services-cards-simple">
        <div class="service-card-simple">
          <div class="service-icon-simple">🔬</div>
          <h3>Clinical Chemistry</h3>
          <p>Blood and urine analysis for disease detection.</p>
        </div>
        <div class="service-card-simple">
          <div class="service-icon-simple">🧬</div>
          <h3>Hematology</h3>
          <p>Blood counts and coagulation studies.</p>
        </div>
        <div class="service-card-simple">
          <div class="service-icon-simple">❤️</div>
          <h3>Cardiology</h3>
          <p>Cardiac testing for early detection.</p>
        </div>
      </div>
    </section>

    <!-- Call to Action Section -->
    <section class="cta-section-simple">
      <h2>Take Control of Your Health</h2>
      <button class="cta-btn-simple">Schedule an Appointment</button>
    </section>

    <!-- Footer -->
    <footer class="footer-simple">
      <div class="footer-links-simple">
        <a href="#">Privacy Policy</a>
        <a href="#">Terms of Service</a>
      </div>
      <div class="footer-copy-simple">© 2024 ClynEra.</div>
    </footer>
  </div>
</template>

<style scoped>
.home-landing-simple {
  background: #fafbfc;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  font-family: 'Inter', Arial, sans-serif;
}

.hero-section-simple {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 180px;
  padding: 32px 8px 16px 8px;
  background: #fff;
  border-bottom: 1px solid #ececec;
}
.hero-content-simple {
  text-align: center;
  max-width: 500px;
  margin: 0 auto;
}
.hero-content-simple h1 {
  font-size: 2rem;
  font-weight: 600;
  color: #222;
  margin-bottom: 12px;
}
.hero-content-simple p {
  color: #555;
  font-size: 1.05rem;
  margin-bottom: 18px;
}
.hero-btn-simple {
  background: #2196f3;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 10px 22px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.2s;
}
.hero-btn-simple:hover {
  background: #1769aa;
}

.services-section-simple {
  max-width: 900px;
  margin: 0 auto;
  padding: 32px 8px 16px 8px;
  text-align: center;
}
.services-section-simple h2 {
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 18px;
  color: #222;
}
.services-cards-simple {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: center;
}
.service-card-simple {
  background: #f5f6fa;
  border-radius: 8px;
  padding: 18px 12px;
  width: 220px;
  text-align: center;
  font-size: 0.98rem;
  color: #333;
  box-shadow: none;
  border: 1px solid #ececec;
}
.service-icon-simple {
  font-size: 1.6rem;
  margin-bottom: 10px;
}
.service-card-simple h3 {
  font-size: 1.08rem;
  font-weight: 500;
  margin-bottom: 6px;
}
.service-card-simple p {
  color: #666;
  font-size: 0.97rem;
}

.cta-section-simple {
  background: #eaf3fa;
  padding: 28px 8px;
  text-align: center;
  margin: 24px 0 0 0;
}
.cta-section-simple h2 {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 14px;
  color: #222;
}
.cta-btn-simple {
  background: #2196f3;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 10px 22px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.2s;
}
.cta-btn-simple:hover {
  background: #1769aa;
}

.footer-simple {
  background: #fafbfc;
  padding: 18px 8px 8px 8px;
  text-align: center;
  color: #888;
  font-size: 0.95rem;
  margin-top: auto;
  border-top: 1px solid #ececec;
}
.footer-links-simple {
  display: flex;
  justify-content: center;
  gap: 18px;
  margin-bottom: 6px;
}
.footer-links-simple a {
  color: #888;
  text-decoration: none;
  transition: color 0.2s;
  font-size: 0.97rem;
}
.footer-links-simple a:hover {
  color: #2196f3;
}
.footer-copy-simple {
  margin-top: 2px;
}

@media (max-width: 700px) {
  .services-cards-simple {
    flex-direction: column;
    align-items: center;
    gap: 10px;
  }
  .service-card-simple {
    width: 95vw;
    padding: 14px 6px;
  }
}
@media (max-width: 500px) {
  .hero-content-simple h1 {
    font-size: 1.2rem;
  }
  .hero-content-simple p {
    font-size: 0.95rem;
  }
  .cta-section-simple h2 {
    font-size: 1rem;
  }
  .cta-btn-simple {
    font-size: 0.95rem;
    padding: 8px 12px;
  }
  .footer-simple {
    font-size: 0.85rem;
    padding: 10px 2px 4px 2px;
  }
  .footer-links-simple {
    gap: 8px;
    flex-direction: column;
    margin-bottom: 4px;
  }
}
</style>
