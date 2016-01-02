# ClamSpeech Format

## Background

The ability to record data in a timestamped, unchangeable manner could benefit many 
applications. ClamSpeech can grant this ability via the Clam blockchain. The subject of this document is 
primarily the format in which ClamSpeeches that are meant to record should be.

Nothing in this document is binding. This document only exists to help coordinate uses of ClamSpeech.

## Format

The suggested format for ClamSpeeches is as follows:

```
appId payload
```

Where:

- `appId`: Purpose identifier.
- `payload`: Relevant data.

## Known appIds

### clamour

`clamour` is used to express support for petitions. ClamSpeeches using this appId are only relevant in 
coinstake transactions. That is, unless staking a block, using this appId is ineffectual.

In coinstake transactions, the ClamSpeech `clamour <petitionID> [<petitionID>, ...]` signifies that the 
staker supports `petitionID`, which is the the first eight hex characters of a petition's SHA256 hash.

### create

`create` is used to establish the fact that data exists in the CLAM blockchain.

Notably, this appId is used to "register" a CLAMour petition. The format is as follows:

```create clamour <petitionHash> [<URL>]```

Where:

- `<petitionHash>` is the SHA256 hash of a petition in hex-encoded format.
- `<URL>` is an optional URL that represents a location the full petition text can be found at.

When two or more petitions have the same petition ID (the first 8 hex characters of the petition hash), 
this is used to determine which is the "real" petition. The petition that was first "registered" with 
the `create` appId is considered the "real" petition.

