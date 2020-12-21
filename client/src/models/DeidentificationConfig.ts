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
    DeidentificationConfigDeidentificationStrategy,
    DeidentificationConfigDeidentificationStrategyFromJSON,
    DeidentificationConfigDeidentificationStrategyFromJSONTyped,
    DeidentificationConfigDeidentificationStrategyToJSON,
} from './';

/**
 * Configuration of one deidentification strategy and a list of annotation types to apply it to.
 * @export
 * @interface DeidentificationConfig
 */
export interface DeidentificationConfig {
    /**
     * The minimum confidence level for a given annotation to be de-identified
     * @type {number}
     * @memberof DeidentificationConfig
     */
    confidenceThreshold?: number;
    /**
     * 
     * @type {DeidentificationConfigDeidentificationStrategy}
     * @memberof DeidentificationConfig
     */
    deidentificationStrategy?: DeidentificationConfigDeidentificationStrategy;
    /**
     * the types of annotations to which the de-identifer should apply the selected strategy
     * @type {Array<string>}
     * @memberof DeidentificationConfig
     */
    annotationTypes?: Array<DeidentificationConfigAnnotationTypesEnum>;
}

export function DeidentificationConfigFromJSON(json: any): DeidentificationConfig {
    return DeidentificationConfigFromJSONTyped(json, false);
}

export function DeidentificationConfigFromJSONTyped(json: any, ignoreDiscriminator: boolean): DeidentificationConfig {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'confidenceThreshold': !exists(json, 'confidenceThreshold') ? undefined : json['confidenceThreshold'],
        'deidentificationStrategy': !exists(json, 'deidentificationStrategy') ? undefined : DeidentificationConfigDeidentificationStrategyFromJSON(json['deidentificationStrategy']),
        'annotationTypes': !exists(json, 'annotationTypes') ? undefined : json['annotationTypes'],
    };
}

export function DeidentificationConfigToJSON(value?: DeidentificationConfig | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'confidenceThreshold': value.confidenceThreshold,
        'deidentificationStrategy': DeidentificationConfigDeidentificationStrategyToJSON(value.deidentificationStrategy),
        'annotationTypes': value.annotationTypes,
    };
}

/**
* @export
* @enum {string}
*/
export enum DeidentificationConfigAnnotationTypesEnum {
    PhysicalAddress = 'text_physical_address',
    Date = 'text_date',
    PersonName = 'text_person_name'
}

