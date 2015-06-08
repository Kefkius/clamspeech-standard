# ClamSpeech Standardized Format

*Everything below is tentative and subject to change.*

## Background

The ability to record an application's state in a timestamped, unchangeable manner could benefit many 
applications. ClamSpeech can grant this ability via the Clam blockchain. The subject of this document is 
primarily the format in which ClamSpeeches that are meant to record state will be.

## Format

Below, "VarInt" refers to a [variable length integer](https://en.bitcoin.it/wiki/Protocol_documentation#Variable_length_integer).

The serialized format of ClamSpeeches that are to be recorded in the blockchain follows:

* 2 bytes: Format version.
* VarInt: Application identifier length.
* (Variable): Application identifier.
* VarInt: Payload (state of the application) length.
* (Variable): Payload.

## Rationale

Variable length integers are used in application identifiers because we make no assumptions about the 
amount of identifiers that will be needed. It's also intuitive to use them in payloads, especially given 
the proposed changes in the "Changes to Clam Client" section.

## Changes to Clam Client

The Clam Client needs to change its rules regarding the validity of clamspeeches. Currently, ClamSpeeches 
above 140 bytes in length are nonstandard, but not invalid. The proposed change would be that:

* "Normal" ClamSpeeches (those that do not record state) should have the version bytes `00` prepended to them.
* ClamSpeeches at or below a certain length threshold remain free.
* ClamSpeeches above the threshold result in a per-byte fee for all bytes after the threshold is reached.
* ClamSpeeches above a certain maximum length are invalid, regardless of fees.

These changes allow ClamSpeeches to occupy as much space as they need, so long as the transaction sender 
is willing to prove that it's necessary by paying a fee.

### Parameters

The threshold for when a fee begins applying, the maximum length regardless of fee, and the fee itself 
have yet to be determined. The behavior of the fee, whether constant for each byte or varying with total 
ClamSpeech length, also needs to be determined.

Given that the size of ClamSpeeches will affect every Clam node, it's necessary to construct reasonable 
restrictions on ClamSpeech length and deterrents for long ClamSpeeches via the above parameters. Input by 
community members is needed.
