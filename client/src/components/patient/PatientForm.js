import React from "react";
import PropTypes from 'prop-types';


export default class PatientForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      firstName: '',
      lastName: '',
      selectedHospitalId: '',
    }

    this.firstNameChanged = this.firstNameChanged.bind(this);
    this.lastNameChanged = this.lastNameChanged.bind(this);
    this.selectedHospitalChanged = this.selectedHospitalChanged.bind(this);
    this.createOrUpdate = this.createOrUpdate.bind(this);
  }

  componentDidUpdate(prevProps) {
    if ((!prevProps.patient && this.props.patient) || (prevProps.patient?.id !== this.props.patient?.id)) {
      this.updateForSelectedPatient();
    }
  }
  
  updateForSelectedPatient() {
    this.setState({
      firstName: this.props.patient ? this.props.patient.first_name : '',
      lastName: this.props.patient ? this.props.patient.last_name : '',
      selectedHospitalId: this.props.patient ? this.props.patient.hospital.id : '',
    })
  }

  firstNameChanged(event) {
    this.setState({firstName: event.target.value})
  }

  lastNameChanged(event) {
    this.setState({lastName: event.target.value})
  }

  selectedHospitalChanged(event) {
    this.setState({selectedHospitalId: event.target.value})
  }

  createOrUpdate() {
    if (this.props.patient) {
      this.props.editHandler(this.props.patient, this.patientPayload);
    } else {
      this.props.createHandler(
        this.state.selectedHospitalId || this.firstHospitalId,
        this.patientPayload,
      );
    }
  }

  get patientPayload() {
    return {
      first_name: this.state.firstName,
      last_name: this.state.lastName,
    }
  }

  get firstHospitalId() {
    return this.props.hospitals ? this.props.hospitals[0].id : null;
  }

  render() {
    return (
      <div className="patient-form">
        <div className="patient-form-section">
          <label>Hospital:</label>
          <select
            value={this.state.selectedHospitalId}
            onChange={this.selectedHospitalChanged}
            disabled={this.props.patient}
          >
            {this.props.hospitals.map(hospital => (
              <option
                key={hospital.id}
                value={hospital.id}
              >
                {hospital.name}
              </option>
            ))}
          </select>
        </div>
        <div className="patient-form-section">
          <label>First Name:</label>
          <input type="text" value={this.state.firstName} onChange={this.firstNameChanged}/>
        </div>
        <div className="patient-form-section">
          <label>Last Name:</label>
          <input type="text" value={this.state.lastName} onChange={this.lastNameChanged}/>
        </div>
        <button 
          className="primary-btn"
          onClick={this.createOrUpdate}
        >
          {this.props.patient ? 'Edit Patient' : 'Create New Patient'}
        </button>
      </div>
    )
  }
};

PatientForm.propTypes = {
  hospitals: PropTypes.array,
  patient: PropTypes.object,
  createHandler: PropTypes.func,
  editHandler: PropTypes.func,
}