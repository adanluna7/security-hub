# 🔒 Security Hub - Repositorio Integral de Seguridad

Un repositorio completo dedicado a seguridad en informática, con herramientas, guías, ejemplos prácticos y recursos educativos sobre criptografía, autenticación, seguridad web, auditoría y análisis de vulnerabilidades.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Módulos Disponibles](#módulos-disponibles)
- [Uso](#uso)
- [Ejemplos](#ejemplos)
- [Documentación](#documentación)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## ✨ Características

- 🔐 **Criptografía**: Algoritmos de cifrado, hashing y firma digital
- 🔑 **Autenticación**: Implementaciones de OAuth2, JWT, 2FA
- 🌐 **Seguridad Web**: Protección contra OWASP Top 10
- 🛡️ **Auditoría**: Herramientas de análisis y compliance
- 🔍 **Análisis de Vulnerabilidades**: Scripts de scaneo y testing
- 📚 **Documentación Completa**: Guías paso a paso
- ⚡ **Ejemplos Prácticos**: Código listo para usar
- 🧪 **Tests Integrados**: Cobertura completa de pruebas

## 📁 Estructura del Proyecto

```
security-hub/
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── .github/
│   ├── workflows/
│   │   ├── security-tests.yml
│   │   ├── code-analysis.yml
│   │   └── vulnerability-scan.yml
│   └── SECURITY.md
├── src/
│   ├── __init__.py
│   ├── cryptography/
│   │   ├── __init__.py
│   │   ├── encryption.py
│   │   ├── hashing.py
│   │   └── digital_signatures.py
│   ├── authentication/
│   │   ├── __init__.py
│   │   ├── jwt_handler.py
│   │   ├── oauth2.py
│   │   ├── two_factor_auth.py
│   │   └── password_utils.py
│   ├── web_security/
│   │   ├── __init__.py
│   │   ├── csrf_protection.py
│   │   ├── xss_prevention.py
│   │   ├── sql_injection_defense.py
│   │   └── headers_security.py
│   ├── audit/
│   │   ├── __init__.py
│   │   ├── logging_auditor.py
│   │   ├── compliance_checker.py
│   │   └── access_control.py
│   └── vulnerability/
│       ├── __init__.py
│       ├── port_scanner.py
│       ├── ssl_checker.py
│       └── dependency_checker.py
├── tests/
│   ├── __init__.py
│   ├── test_cryptography.py
│   ├── test_authentication.py
│   ├── test_web_security.py
│   ├── test_audit.py
│   └── test_vulnerability.py
├── docs/
│   ├── GUÍA_CRIPTOGRAFÍA.md
│   ├── GUÍA_AUTENTICACIÓN.md
│   ├── GUÍA_SEGURIDAD_WEB.md
│   ├── GUÍA_AUDITORÍA.md
│   ├── GUÍA_VULNERABILIDADES.md
│   ├── OWASP_TOP_10.md
│   └── MEJORES_PRÁCTICAS.md
├── examples/
│   ├── crypto_examples.py
│   ├── auth_examples.py
│   ├── web_security_examples.py
│   └── audit_examples.py
└── config/
    ├── security_config.yaml
    └── logging_config.yaml
```

## 🚀 Instalación

### Requisitos previos
- Python 3.8+
- pip o poetry
- Git

### Pasos de instalación

```bash
# Clonar el repositorio
git clone https://github.com/adanluna7/security-hub.git
cd security-hub

# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar tests
pytest tests/ -v
```

## 📦 Módulos Disponibles

### 1. **Criptografía** (`src/cryptography/`)
- Cifrado AES, RSA, DES
- Hashing (SHA-256, SHA-512, bcrypt)
- Firma digital
- Generación de claves seguras

### 2. **Autenticación** (`src/authentication/`)
- Manejo de JWT tokens
- OAuth2 flow
- Two-Factor Authentication (2FA)
- Validación de contraseñas
- Session management

### 3. **Seguridad Web** (`src/web_security/`)
- Protección CSRF
- Prevención XSS
- Defensa contra SQL Injection
- Security headers
- CORS configuration

### 4. **Auditoría** (`src/audit/`)
- Logging de eventos de seguridad
- Verificación de compliance
- Control de acceso
- Análisis de permisos

### 5. **Análisis de Vulnerabilidades** (`src/vulnerability/`)
- Escaneo de puertos
- Verificación SSL/TLS
- Análisis de dependencias
- Detección de vulnerabilidades conocidas

## 💻 Uso

### Ejemplo básico: Cifrado

```python
from src.cryptography.encryption import AESCipher

# Crear instancia
cipher = AESCipher()

# Cifrar datos
plaintext = "Información sensible"
ciphertext = cipher.encrypt(plaintext)
print(f"Cifrado: {ciphertext}")

# Descifrar
decrypted = cipher.decrypt(ciphertext)
print(f"Descifrado: {decrypted}")
```

### Ejemplo: Autenticación JWT

```python
from src.authentication.jwt_handler import JWTHandler

handler = JWTHandler(secret="tu_secreto_seguro")

# Crear token
token = handler.create_token(user_id="user123", expires_in=3600)

# Verificar token
payload = handler.verify_token(token)
print(f"Usuario: {payload['user_id']}")
```

### Ejemplo: Protección CSRF

```python
from src.web_security.csrf_protection import CSRFProtection

csrf = CSRFProtection()

# Generar token
token = csrf.generate_token()

# Validar token
is_valid = csrf.validate_token(token)
print(f"Token válido: {is_valid}")
```

## 📚 Documentación

Consulta la carpeta `docs/` para guías detalladas:

- **[GUÍA_CRIPTOGRAFÍA.md](docs/GUÍA_CRIPTOGRAFÍA.md)** - Conceptos y ejemplos de criptografía
- **[GUÍA_AUTENTICACIÓN.md](docs/GUÍA_AUTENTICACIÓN.md)** - Implementación de sistemas de autenticación
- **[GUÍA_SEGURIDAD_WEB.md](docs/GUÍA_SEGURIDAD_WEB.md)** - Protección de aplicaciones web
- **[GUÍA_AUDITORÍA.md](docs/GUÍA_AUDITORÍA.md)** - Logging y compliance
- **[GUÍA_VULNERABILIDADES.md](docs/GUÍA_VULNERABILIDADES.md)** - Análisis y scanning
- **[OWASP_TOP_10.md](docs/OWASP_TOP_10.md)** - Top 10 vulnerabilidades web
- **[MEJORES_PRÁCTICAS.md](docs/MEJORES_PRÁCTICAS.md)** - Recomendaciones de seguridad

## 🧪 Testing

```bash
# Ejecutar todos los tests
pytest tests/ -v

# Con cobertura
pytest tests/ --cov=src --cov-report=html

# Test específico
pytest tests/test_cryptography.py -v
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

## 🔐 Seguridad

Si encuentras una vulnerabilidad, por favor reportala responsablemente en [SECURITY.md](.github/SECURITY.md) en lugar de usar el issue tracker público.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

## 📞 Contacto

- **Autor**: Adan Luna
- **Email**: contacto@adanluna.dev
- **GitHub**: [@adanluna7](https://github.com/adanluna7)

---

**⭐ Si este proyecto te fue útil, considera darle una estrella!**

Última actualización: 2026-06-07