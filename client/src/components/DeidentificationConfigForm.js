import React from 'react';
import { DeidentificationConfigAnnotationTypesEnum } from '../models';
import { FormControl, FormHelperText, InputLabel, Fab, Select, MenuItem, TextField, Grid, Typography } from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';
import CloseIcon from '@material-ui/icons/Close';

const styles = (theme) => ({
  maskingCharField: {
    width: "40px",
    textAlign: "center"
  }
});

export class DeidentificationConfigForm extends React.Component {
  updateDeidConfig = (newSettings) => {
    this.props.updateDeidConfig(this.props.index, newSettings);
  }

  handleStrategyChange = (event) => {
    // Convert strategy name into correct {key: value} pair
    const newDeidStrategyName = event.target.value;
    let newDeidentificationStrategy = {};
    // FIXME: Ideally this could draw on the models defined in src/models
    if (newDeidStrategyName === "maskingCharConfig") {
      newDeidentificationStrategy[newDeidStrategyName] = { maskingChar: "*" };
    } else {
      newDeidentificationStrategy[newDeidStrategyName] = {}
    }

    // Push up the state
    this.updateDeidConfig({
      deidentificationStrategy: newDeidentificationStrategy
    });
  }

  handleMaskingCharChange = (event) => {
    const maskingChar = event.target.value;
    this.updateDeidConfig({
      deidentificationStrategy: {
        maskingCharConfig: { maskingChar: maskingChar }
      }
    });
  }

  handleConfidenceThresholdChange = (event) => {
    this.updateDeidConfig({
      confidenceThreshold: parseFloat(event.target.value)
    });
  }

  handleAnnotationTypeDelete = (event, index) => {
    const annotationTypes = this.props.annotationTypes
    const newAnnotationTypes = annotationTypes.slice(0, index).concat(annotationTypes.slice(index+1));
    this.updateDeidConfig({
      annotationTypes: newAnnotationTypes
    });
  }

  handleAnnotationTypeAdd = (event) => {
    const annotationType = event.target.value;
    this.updateDeidConfig({
      annotationTypes: this.props.annotationTypes.concat(annotationType)
    });
  }

  handleDelete = () => {
    this.props.deleteDeidConfig(this.props.index);
  }

  getStrategy = () => {
    return Object.keys(this.props.deidentificationStrategy)[0];
  }

  render = () => {
    const { classes } = this.props;
    const allAnnotationTypes = Object.values(DeidentificationConfigAnnotationTypesEnum)
    return (
      <Grid item container direction="column">
        <Grid item>
          <Typography variant="h6">De-id Step #{this.props.index + 1}</Typography>
        </Grid>
        <Grid item>
          <Select label="Method" onChange={this.handleStrategyChange} value={this.getStrategy()}>
            <MenuItem value="maskingCharConfig">Masking Character</MenuItem>
            <MenuItem value="redactConfig">Redact</MenuItem>
            <MenuItem value="annotationTypeConfig">Annotation Type</MenuItem>
          </Select>
          &nbsp;
          {this.getStrategy() === "maskingCharConfig" &&
            <TextField
              variant="outlined"
              size="small"
              value={this.props.deidentificationStrategy.maskingCharConfig.maskingChar}
              onChange={this.handleMaskingCharChange}
              className={classes.maskingCharField}
              inputProps={{maxLength: 1, style: { textAlign: "center" }}}
            />
          }
        </Grid>
        <Grid item>
          <TextField label="Confidence Threshold" type="number" onChange={this.handleConfidenceThresholdChange} name="confidenceThreshold" value={this.props.confidenceThreshold} />
        </Grid>
        <Grid item>
          Annotation types:
          <div>
            {this.props.annotationTypes.map((annotationType, index) => {
              return (
                <div>{annotationType} <button onClick={(event) => {this.handleAnnotationTypeDelete(event, index);}}> - </button></div>
              );
            })}
            {this.props.annotationTypes.length < allAnnotationTypes.length &&
              <FormControl>
                <InputLabel>Annotation type</InputLabel>
                <Select value="" onChange={this.handleAnnotationTypeAdd}>
                  <MenuItem value=""></MenuItem>
                  {allAnnotationTypes.filter(annotationType => !this.props.annotationTypes.includes(annotationType)).map((annotationType) => {
                    return (
                      <MenuItem value={annotationType}>{annotationType}</MenuItem>
                    );
                  })}
                </Select>
                <FormHelperText>Click to add</FormHelperText>
              </FormControl>
            }
          </div>
        </Grid>
        <Grid item>
          <Fab onClick={this.handleDelete} size="medium"><CloseIcon /></Fab>
        </Grid>
      </Grid>
    );
  }
}

export default withStyles(styles)(DeidentificationConfigForm);
