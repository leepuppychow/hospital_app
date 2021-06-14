import React from "react";
import PropTypes from 'prop-types';


export default class HospitalIndex extends React.Component {
  render() {
    return (<div>
      <h1>**** UNDER CONSTRUCTION ****</h1>
      <h2>Hospital Index</h2>
      {this.props.hospitals.map(hospital => (
        <p key={hospital.id}>{hospital.name}</p>
      ))}
    </div>
    )
  }
};

HospitalIndex.propTypes = {
  hospitals: PropTypes.array,
}