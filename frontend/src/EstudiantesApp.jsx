import { useState, useEffect } from 'react';
import { read, create, update, deleteE } from './services/api';
import DataTable from 'react-data-table-component';
import 'bootstrap/dist/css/bootstrap.min.css';
import toast, { Toaster } from 'react-hot-toast';

export default function EstudiantesApp() {
    const [estudiantes, setEstudiantes] = useState([]);
    const [formData, setFormData] = useState({ nombre: '', matricula: '', edad: '', carrera: '', promedio: '' });
    const [editandoId, setEditandoId] = useState(null);
    const [filtro, setFiltro] = useState('');
    const [cargandoTabla, setCargandoTabla] = useState(false);
    const [cargandoGuardar, setCargandoGuardar] = useState(false);
    const [erroresBackend, setErroresBackend] = useState({});

    useEffect(() => {
        cargarEstudiantes();
    }, []);

    const cargarEstudiantes = async () => {
        setCargandoTabla(true);
        try {
            const respuesta = await read();
            setEstudiantes(respuesta.data);
        } catch (error) {
            console.error("Error al cargar estudiantes:", error);
            toast.error("Error al obtener los datos del servidor");
        } finally {
            setCargandoTabla(false);
        }
    };

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setCargandoGuardar(true);
        setErroresBackend({});

        await new Promise(resolve => setTimeout(resolve, 500)); 

        try {
            if (editandoId) {
                await update(editandoId, formData);
                toast.success("Estudiante actualizado correctamente");
            } else {
                await create(formData);
                toast.success("Estudiante registrado exitosamente");
            }

            setFormData({ nombre: '', matricula: '', edad: '', carrera: '', promedio: '' });
            setEditandoId(null);
            cargarEstudiantes();

        } catch (error) {
            console.error("Error al guardar:", error);
            if (error.response && error.response.data) {
                setErroresBackend(error.response.data); // Guardamos los errores por campo
                toast.error("Por favor, corrige los errores en el formulario");
            } else {
                toast.error("Hubo un error de conexión con el servidor");
            }        
        } finally {
            setCargandoGuardar(false);
        }
    };

    const prepararEdicion = (estudiante) => {
        setFormData({
            nombre: estudiante.nombre,
            matricula: estudiante.matricula,
            edad: estudiante.edad,
            carrera: estudiante.carrera,
            promedio: estudiante.promedio
        });
        setEditandoId(estudiante.id);
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    const handleEliminar = async (id) => {
        if (window.confirm("¿Seguro que deseas eliminar a este estudiante?")) {
            const toastId = toast.loading("Eliminando estudiante..."); 
            try {
                await deleteE(id);
                toast.success("Estudiante eliminado", { id: toastId });
                cargarEstudiantes(); 
            } catch (error) {
                console.error("Error al eliminar:", error);
                toast.error("Error al eliminar al estudiante", { id: toastId });
            }
        }
    };

    const estudiantesFiltrados = estudiantes.filter(
        estudiante => 
            estudiante.nombre.toLowerCase().includes(filtro.toLowerCase()) || 
            estudiante.matricula.toLowerCase().includes(filtro.toLowerCase())
    );

    const barraDeBusqueda = (
        <div className="input-group mb-3" style={{ maxWidth: '300px' }}>
            <input
                type="text"
                className="form-control"
                placeholder="Buscar nombre o matrícula..."
                value={filtro}
                onChange={(e) => setFiltro(e.target.value)}
            />
            {filtro && (
                <button className="btn btn-outline-secondary" type="button" onClick={() => setFiltro('')}>
                    ✖
                </button>
            )}
        </div>
    );

    const SpinnerTabla = () => (
        <div className="p-5 text-center">
            <div className="spinner-border text-primary" role="status">
                <span className="visually-hidden">Cargando...</span>
            </div>
            <p className="mt-2 text-muted">Cargando registros...</p>
        </div>
    );

    const columnas = [
        { name: 'Nombre', selector: row => row.nombre, sortable: true },
        { name: 'Matrícula', selector: row => row.matricula, sortable: true },
        { name: 'Edad', selector: row => row.edad, sortable: true },
        { name: 'Carrera', selector: row => row.carrera, sortable: true },
        { name: 'Promedio', selector: row => row.promedio, sortable: true },
        {
            name: 'Acciones',
            cell: row => (
                <div className="d-flex gap-2">
                    <button className="btn btn-warning btn-sm" onClick={() => prepararEdicion(row)} disabled={cargandoTabla}>
                        ✏️ Editar
                    </button>
                    <button className="btn btn-danger btn-sm" onClick={() => handleEliminar(row.id)} disabled={cargandoTabla}>
                        🗑️ Eliminar
                    </button>
                </div>
            ),
            ignoreRowClick: true,
            allowOverflow: true,
            button: true,
        },
    ];

    return (
        <div className="container mt-5">
            <Toaster position="top-right" reverseOrder={false} /> 

            <div className="row">
                <div className="col-md-4 mb-4">
                    <div className="card shadow-sm">
                        <div className="card-header bg-primary text-white">
                            <h5 className="mb-0">{editandoId ? 'Editar Estudiante' : 'Registrar Estudiante'}</h5>
                        </div>
                        <div className="card-body">
                            <form onSubmit={handleSubmit}>
                                <div className="mb-3">
                                    <label className="form-label">Nombre</label>
                                    <input 
                                        type="text" 
                                        name="nombre" 
                                        className={`form-control ${erroresBackend.nombre ? 'is-invalid' : ''}`} 
                                        value={formData.nombre} 
                                        onChange={handleChange} 
                                        required 
                                        disabled={cargandoGuardar} 
                                    />
                                    {erroresBackend.nombre && (
                                        <div className="invalid-feedback">
                                            {erroresBackend.nombre.join(', ')}
                                        </div>
                                    )}                                
                                </div>
                                <div className="mb-3">
                                    <label className="form-label">Matrícula</label>
                                    <input 
                                        type="text" 
                                        name="matricula" 
                                        className={`form-control ${erroresBackend.matricula ? 'is-invalid' : ''}`} 
                                        value={formData.matricula} 
                                        onChange={handleChange} 
                                        required 
                                        disabled={cargandoGuardar} 
                                    />
                                    {erroresBackend.matricula && (
                                        <div className="invalid-feedback">
                                            {erroresBackend.matricula.join(', ')}
                                        </div>
                                    )}                                
                                </div>
                                <div className="mb-3">
                                    <label className="form-label">Edad</label>
                                    <input 
                                        type="number" 
                                        name="edad" 
                                        className={`form-control ${erroresBackend.edad ? 'is-invalid' : ''}`} 
                                        value={formData.edad} 
                                        onChange={handleChange} 
                                        required 
                                        disabled={cargandoGuardar} 
                                    />
                                    {erroresBackend.edad && (
                                        <div className="invalid-feedback">
                                            {erroresBackend.edad.join(', ')}
                                        </div>
                                    )}                                
                                </div>
                                <div className="mb-3">
                                    <label className="form-label">Carrera</label>
                                    <input 
                                        type="text" 
                                        name="carrera" 
                                        className={`form-control ${erroresBackend.carrera ? 'is-invalid' : ''}`} 
                                        value={formData.carrera} 
                                        onChange={handleChange} 
                                        required 
                                        disabled={cargandoGuardar} 
                                    />
                                    {erroresBackend.carrera && (
                                        <div className="invalid-feedback">
                                            {erroresBackend.carrera.join(', ')}
                                        </div>
                                    )}                                
                                </div>
                                <div className="mb-3">
                                    <label className="form-label">Promedio</label>
                                    <input 
                                        type="number" 
                                        step="0.01"
                                        name="promedio" 
                                        className={`form-control ${erroresBackend.promedio ? 'is-invalid' : ''}`} 
                                        value={formData.promedio} 
                                        onChange={handleChange} 
                                        required 
                                        disabled={cargandoGuardar} 
                                    />
                                    {erroresBackend.promedio && (
                                        <div className="invalid-feedback">
                                            {erroresBackend.promedio.join(', ')}
                                        </div>
                                    )}                                
                                </div>
                                <div className="d-grid gap-2">
                                    <button type="submit" className="btn btn-success" disabled={cargandoGuardar}>
                                        {cargandoGuardar ? (
                                            <><span className="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Guardando...</>
                                        ) : (
                                            editandoId ? 'Actualizar' : 'Guardar'
                                        )}
                                    </button>
                                    {editandoId && (
                                        <button type="button" className="btn btn-secondary" onClick={() => { setEditandoId(null); setFormData({ nombre: '', matricula: '', edad: '', carrera: '', promedio: '' }); setErroresBackend({}); }} disabled={cargandoGuardar}>
                                            Cancelar
                                        </button>
                                    )}
                                </div>
                            </form>
                        </div>
                    </div>
                </div>

                <div className="col-md-8">
                    <div className="card shadow-sm">
                        <div className="card-body p-0 pt-3">
                            <DataTable
                                title="Lista de Estudiantes"
                                columns={columnas}
                                data={estudiantesFiltrados}
                                pagination
                                paginationPerPage={5}
                                highlightOnHover
                                responsive
                                subHeader
                                subHeaderComponent={barraDeBusqueda}
                                subHeaderAlign="right"
                                noDataComponent="No hay estudiantes que coincidan con la búsqueda"                             
                                progressPending={cargandoTabla}
                                progressComponent={<SpinnerTabla />}
                            />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
