import { readFile } from 'node:fs/promises';

export async function readText(input) {
  return await readFile(input, 'utf8'); 
}

export function manageMultipleLines(input) {    
    return input.replace(/\r\n?/g, '\n').trimEnd().split('\n');
}