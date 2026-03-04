import axios from 'axios';

// La URL base para estudiantes
const BASE_URL = 'http://localhost:8000/estudiantes'; 

// 1. LISTAR (GET)
export const read = () => {
    return axios.get(`${BASE_URL}/`);
};

// 2. CREAR (POST)
export const create = (data) => {
    // Si la API acepta JSON directo (DRF lo hace por defecto sin FormData)
    // Pero seguiremos la estructura del ejemplo con FormData
    const formData = new FormData();
    for (const key in data) {
        formData.append(key, data[key]);
    }
    return axios.post(`${BASE_URL}/`, formData);
};

// 3. ACTUALIZAR (PUT)
export const update = (id, data) => {
    const formData = new FormData();
    for (const key in data) {
        formData.append(key, data[key]);
    }
    return axios.put(`${BASE_URL}/${id}/`, formData);
};

// 4. ELIMINAR (DELETE)
export const deleteE = (id) => {
    return axios.delete(`${BASE_URL}/${id}/`);
};
