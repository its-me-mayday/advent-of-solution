import { readFile } from 'node:fs/promises';

export async function readText(path) {
  return await readFile(path, 'utf8'); 
}