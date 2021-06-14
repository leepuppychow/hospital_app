export default function PatientCard(props) {
  return (
    <div key={props.patient.id}>
      {props.patient.first_name} {props.patient.last_name}: {props.patient.hospital.name}
      <button onClick={() => props.selectedPatientHandler(props.patient)}>
        Edit
      </button>
      <button onClick={() => props.deleteHandler(props.patient)}>
        Delete
      </button>
    </div>
  )
} 