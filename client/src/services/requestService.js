import 'axios';
import axios from 'axios';

const HOST = 'http://localhost:5000'

export const getHospitals = () => {
  return axios.get(`${HOST}/api/v1/hospitals`);
}

export const deletePatient = (patient) => {
  return axios.delete(`${HOST}/api/v1/hospitals/${patient.hospital.id}/patients/${patient.id}`);
}

export const createPatient = (idHospital, payload) => {
  return axios.post(`${HOST}/api/v1/hospitals/${idHospital}/patients`, payload);
}

export const updatePatient = (patient, payload) => {
  return axios.put(`${HOST}/api/v1/hospitals/${patient.hospital.id}/patients/${patient.id}`, payload);
}