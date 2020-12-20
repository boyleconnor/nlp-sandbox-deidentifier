/* tslint:disable */
/* eslint-disable */
/**
 * NLP Sandbox Deidentifier API
 * The OpenAPI specification implemented by NLP Sandbox PHI Deidentifiers. # Overview TBA 
 *
 * The version of the OpenAPI document: 0.2.2
 * Contact: thomas.schaffter@sagebionetworks.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import {
    DeidentificationConfig,
    DeidentificationConfigFromJSON,
    DeidentificationConfigFromJSONTyped,
    DeidentificationConfigToJSON,
    Note,
    NoteFromJSON,
    NoteFromJSONTyped,
    NoteToJSON,
} from './';

/**
 * A request to de-identify a note
 * @export
 * @interface DeidentifyRequest
 */
export interface DeidentifyRequest {
    /**
     * A list of deidentification strategies and the entity types on which to perform them. De-identification priority (i.e. which annotation to use when two annotations overlap) is determined by the order of this array and the order of the annotationTypes array inside of each deidentificationConfig.
     * @type {Array<DeidentificationConfig>}
     * @memberof DeidentifyRequest
     */
    deidentificationConfigurations?: Array<DeidentificationConfig>;
    /**
     * 
     * @type {Note}
     * @memberof DeidentifyRequest
     */
    note: Note;
}

export function DeidentifyRequestFromJSON(json: any): DeidentifyRequest {
    return DeidentifyRequestFromJSONTyped(json, false);
}

export function DeidentifyRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): DeidentifyRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'deidentificationConfigurations': !exists(json, 'deidentificationConfigurations') ? undefined : ((json['deidentificationConfigurations'] as Array<any>).map(DeidentificationConfigFromJSON)),
        'note': NoteFromJSON(json['note']),
    };
}

export function DeidentifyRequestToJSON(value?: DeidentifyRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'deidentificationConfigurations': value.deidentificationConfigurations === undefined ? undefined : ((value.deidentificationConfigurations as Array<any>).map(DeidentificationConfigToJSON)),
        'note': NoteToJSON(value.note),
    };
}

