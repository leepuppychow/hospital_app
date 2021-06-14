import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import HospitalIndex from "./components/hospital/HospitalIndex";
import PatientIndex from "./components/patient/PatientIndex";
import { getHospitals } from './services/requestService'

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      hospitals: [],
    }
    this.reloadHospitalData = this.reloadHospitalData.bind(this);
  }

  async componentDidMount() {
    this.reloadHospitalData();
  }

  async reloadHospitalData() {
    try {
      const res = await getHospitals();
      if (res.data) this.setState({hospitals: res.data});
    } catch (error) {
      console.error(error);
    }
  }

  render() {
    return (
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/hospitals">Hospitals</Link>
              </li>
              <li>
                <Link to="/patients">Patients</Link>
              </li>
            </ul>
          </nav>
  
          <Switch>
            <Route
              path="/hospitals"
              render={() => (
                <HospitalIndex
                  hospitals={this.state.hospitals}
                  reload={this.reloadHospitalData}
                />
              )}
            />
            <Route
              path="/patients"
              render={() => (
                <PatientIndex 
                  hospitals={this.state.hospitals}
                  reload={this.reloadHospitalData}
                />
              )}
            />
          </Switch>
        </div>
      </Router>
    );
  }
}
