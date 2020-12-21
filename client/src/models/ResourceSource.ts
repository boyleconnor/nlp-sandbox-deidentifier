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
/**
 * An API resource source
 * @export
 * @interface ResourceSource
 */
export interface ResourceSource {
    /**
     * Full path of an API resource
     * @type {string}
     * @memberof ResourceSource
     */
    name?: string;
}

export function ResourceSourceFromJSON(json: any): ResourceSource {
    return ResourceSourceFromJSONTyped(json, false);
}

export function ResourceSourceFromJSONTyped(json: any, ignoreDiscriminator: boolean): ResourceSource {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'name': !exists(json, 'name') ? undefined : json['name'],
    };
}

export function ResourceSourceToJSON(value?: ResourceSource | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'name': value.name,
    };
}

