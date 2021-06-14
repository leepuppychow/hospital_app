import React from "react";
import PropTypes from 'prop-types';

import PatientCard from "./PatientCard";
import PatientForm from "./PatientForm";
import { 
  deletePatient,
  createPatient,
  updatePatient,
} from '../../services/requestService';


export default class PatientIndex extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedPatient: null,
    }

    this.setSelectedPatient = this.setSelectedPatient.bind(this);
    this.deletePatientHandler = this.deletePatientHandler.bind(this);
    this.createPatientHandler = this.createPatientHandler.bind(this);
    this.editPatientHandler = this.editPatientHandler.bind(this);
  }

  get patients() {
    return this.props.hospitals
      .reduce((acc, hospital) => {
        const patients = hospital.patients.map(p => ({...p, hospital}))
        return [...acc, ...patients];
      }, [])
  }

  setSelectedPatient(patient) {
    this.setState({selectedPatient: patient});
  }

  async deletePatientHandler(patient) {
    if (window.confirm("Are you sure you want to delete this patient?")) {
      await deletePatient(patient);
      await this.props.reload();
    }
  }

  async createPatientHandler(idHospital, payload) {
    await createPatient(idHospital, payload);
    await this.props.reload();
  }

  async editPatientHandler(patient, payload) {
    await updatePatient(patient, payload);
    await this.props.reload();
  }

  render() {
    return (
      <div className="patient-index">
        <h2>Patient Index</h2>
        <PatientForm 
          patient={this.state.selectedPatient}
          hospitals={this.props.hospitals}
          createHandler={this.createPatientHandler}
          editHandler={this.editPatientHandler}
        />
        <h5>*** TODO: add filtering and sorting functionality ***</h5>
        {this.patients.map(patient => (
          <PatientCard
            key={patient.id}
            patient={patient}
            selectedPatientHandler={this.setSelectedPatient}
            deleteHandler={this.deletePatientHandler}
          />
        ))}
      </div>
    )
  }
};

PatientIndex.propTypes = {
  hospitals: PropTypes.array,
  reload: PropTypes.func,
}