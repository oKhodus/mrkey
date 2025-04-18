
## 🚧 Marketplace Project Roadmap (Django)

### ✅ 1. Models
**Goal:** Create basic database tables for products and orders
- [x] Product — product model
- [x] Order — order model
- [x] Category — product categories *(optional)*
- [x] Review — product reviews *(optional)*
- [x] ShippingInfo — shipping data *(if needed)*

**Process:**
1. Define fields and relationships in `models.py`
2. Run migrations using `makemigrations` and `migrate`
3. [x] Check functionality in Django admin

---

### 🔄 2. API
**Goal:** Provide access to models via REST API
- [x] Serializers for Product and Order
- [x] ViewSets and routes
- [x] Access restriction (only the author can edit the product)
- [x/-] Filtering and search (by category, price, etc.)
- [x] Pagination

**Process:**
1. Create `serializers.py` and define serializers
2. Use ViewSets + Router in `views.py` and `urls.py`
3. Add permissions using `permissions.py`
4. Add filtering and pagination using `DjangoFilterBackend`

---

### 🔑 3. Authentication and Authorization
**Goal:** Manage users and access control
- [ ] User registration and login
- [ ] JWT tokens (`djangorestframework-simplejwt`)
- [ ] User roles: buyer/seller

**Process:**
1. Install and configure `djoser` or custom auth views
2. Enable JWT
3. Assign permissions in serializers and views

---

### 💸 4. Payments *(optional)*
**Goal:** Implement payment functionality
- [ ] Integrate payment system (e.g., Stripe)
- [ ] Payment status field (`is_paid`)

**Process:**
1. Register on Stripe/PayPal
2. Integrate SDK and configure webhooks
3. Update `is_paid` field on successful payment

---

### 🖼 5. Frontend
**Goal:** Display products and handle orders
- [ ] Home page: product list
- [ ] Product detail page
- [ ] Cart
- [ ] Checkout process

*(Use Django templates, React, or HTMX — your choice)*

**Process:**
1. Choose frontend technology (HTML/JS or SPA)
2. Build basic templates/components
3. Connect to API using fetch/axios

---

### 🚀 6. Deployment
**Goal:** Deploy project online
- [ ] Docker + Docker Compose
- [ ] PostgreSQL
- [ ] Hosting (Render / Railway / Vercel / VPS)

**Process:**
1. Create Dockerfile and `docker-compose.yml`
2. Setup `.env` and SECRET_KEY
3. Deploy to chosen hosting

---

### 🧩 Extras (as project grows)
- [ ] Favorites / Likes
- [ ] Admin dashboard for sellers
- [ ] Notifications
- [ ] SEO + meta tags
