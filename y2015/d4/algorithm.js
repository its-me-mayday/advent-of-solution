import crypto from 'node:crypto';

const re = /^0{5,}/;
const re6z = /^0{6,}/;

function md5(text) {
  return crypto.createHash('md5').update(text).digest('hex');
}

function isAnAccettableHash(hash) {
  return typeof hash === 'string' && re.test(hash);
}

function isAnAccettableHashSixZeros(hash) {
  return typeof hash === 'string' && re6z.test(hash);
}

export function getHashAdventCoinPayload(secret) {
    let hashAdventCoin = md5(secret);
    let payload = 0;
    
    console.log(isAnAccettableHash(hashAdventCoin))

    if(!isAnAccettableHash(hashAdventCoin)){
        console.log("Searching payload...")
       do {
           let secretManipulated = `${secret}${payload}`
           hashAdventCoin = md5(secretManipulated)
           payload += 1

       }while(!isAnAccettableHash(hashAdventCoin));
    }
    else
        return payload

    console.log(`The hash that starts with at least 5 zeros is: ${hashAdventCoin}`)
    console.log(`The entire secret is: ${secret}${payload-1}`)
    return payload-1;
}

export function getHashAdventCoinPayloadSixZeros(secret) {
    let hashAdventCoin = md5(secret);
    let payload = 0;
    
    console.log(isAnAccettableHashSixZeros(hashAdventCoin))

    if(!isAnAccettableHashSixZeros(hashAdventCoin)){
        console.log("Searching payload...")
       do {
           let secretManipulated = `${secret}${payload}`
           hashAdventCoin = md5(secretManipulated)
           payload += 1

       }while(!isAnAccettableHashSixZeros(hashAdventCoin));
    }
    else
        return payload

    console.log(`The hash that starts with at least 5 zeros is: ${hashAdventCoin}`)
    console.log(`The entire secret is: ${secret}${payload-1}`)
    return payload-1;
}