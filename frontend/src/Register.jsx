import { useState } from "react";
import axios from "axios"; // Usamos axios puro para el registro inicial
import toast, { Toaster } from "react-hot-toast";
import "bootstrap/dist/css/bootstrap.min.css";

export default function Register({ onGoToLogin }) {
  const [formData, setFormData] = useState({
    email: "",
    nombre_completo: "",
    password: "",
    telefono: "",
  });
  const [cargando, setCargando] = useState(false);
  const [erroresBackend, setErroresBackend] = useState({});

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setCargando(true);
    setErroresBackend({});

    try {
      // POST a la ruta que configuramos en usuarios -> urls.py
      await axios.post("http://localhost:8000/usuarios/registro/", formData);

      toast.success("¡Registro exitoso! Por favor inicia sesión.");
      
      // Esperamos 2 segundos y redirigimos manual al login
      setTimeout(() => {
        onGoToLogin();
      }, 2000);

    } catch (error) {
      console.error("Error en registro:", error);
      if (error.response && error.response.data) {
        setErroresBackend(error.response.data);
        toast.error("Por favor, corrige los errores en el formulario");
      } else {
        toast.error("Error al conectar con el servidor");
      }
    } finally {
      setCargando(false);
    }
  };

  return (
    <div className="container mt-5">
      <Toaster position="top-right" reverseOrder={false} />
      
      <div className="row justify-content-center">
        <div className="col-md-5">
          <div className="card shadow-sm mt-5">
            <div className="card-header bg-success text-white text-center">
              <h4 className="mb-0">Crear Cuenta</h4>
            </div>
            <div className="card-body p-4">
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label className="form-label">Correo Electrónico (Login)</label>
                  <input
                    type="email"
                    name="email"
                    className={`form-control ${erroresBackend.email ? "is-invalid" : ""}`}
                    value={formData.email}
                    onChange={handleChange}
                    required
                    disabled={cargando}
                  />
                  {erroresBackend.email && (
                    <div className="invalid-feedback">{erroresBackend.email.join(", ")}</div>
                  )}
                </div>

                <div className="mb-3">
                  <label className="form-label">Nombre Completo</label>
                  <input
                    type="text"
                    name="nombre_completo"
                    className={`form-control ${erroresBackend.nombre_completo ? "is-invalid" : ""}`}
                    value={formData.nombre_completo}
                    onChange={handleChange}
                    required
                    disabled={cargando}
                  />
                  {erroresBackend.nombre_completo && (
                    <div className="invalid-feedback">{erroresBackend.nombre_completo.join(", ")}</div>
                  )}
                </div>
                
                <div className="mb-3">
                  <label className="form-label">Contraseña</label>
                  <input
                    type="password"
                    name="password"
                    className={`form-control ${erroresBackend.password ? "is-invalid" : ""}`}
                    value={formData.password}
                    onChange={handleChange}
                    required
                    disabled={cargando}
                  />
                  {erroresBackend.password && (
                    <div className="invalid-feedback">{erroresBackend.password.join(", ")}</div>
                  )}
                </div>

                <div className="mb-4">
                  <label className="form-label">Teléfono (Opcional)</label>
                  <input
                    type="text"
                    name="telefono"
                    className={`form-control ${erroresBackend.telefono ? "is-invalid" : ""}`}
                    value={formData.telefono}
                    onChange={handleChange}
                    disabled={cargando}
                  />
                  {erroresBackend.telefono && (
                    <div className="invalid-feedback">{erroresBackend.telefono.join(", ")}</div>
                  )}
                </div>

                <div className="d-grid gap-2 mb-3">
                  <button 
                    type="submit" 
                    className="btn btn-success btn-lg"
                    disabled={cargando}
                  >
                    {cargando ? (
                      <>
                        <span className="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                        Registrando...
                      </>
                    ) : (
                      "Registrarme"
                    )}
                  </button>
                </div>

                <div className="text-center">
                    <p className="mb-0">¿Ya tienes cuenta?</p>
                    <button 
                        type="button" 
                        className="btn btn-link p-0" 
                        onClick={onGoToLogin}
                        disabled={cargando}
                    >
                        Inicia sesión aquí
                    </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
