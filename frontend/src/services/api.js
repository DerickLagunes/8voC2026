import axios from 'axios';

// La URL base para estudiantes
const BASE_URL = 'http://localhost:8000/estudiantes'; 

// 1. LISTAR (GET)
export const read = () => {
    return axios.get(`${BASE_URL}/`);
};

// 2. CREAR (POST)
export const create = (data) => {
    return axios.post(`${BASE_URL}/`, data);
};

// 3. ACTUALIZAR (PUT)
export const update = (id, data) => {
    return axios.put(`${BASE_URL}/${id}/`, data);
};

// 4. ELIMINAR (DELETE)
export const deleteE = (id) => {
    return axios.delete(`${BASE_URL}/${id}/`);
};
