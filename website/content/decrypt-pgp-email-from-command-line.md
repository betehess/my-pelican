Title: How to read a PGP-encrypted email from the command-line 
Date: 2015-02-21
Slug: decrypt-pgp-email-from-command-line

I received a PGP-encrypted email a couple days ago with confidential information. As I use GMail, I do not have direct support for PGP. Here are the steps I followed in order to extract the message and the files in it, from the command-line.

Disclaimer: I already knew the [big picture for PGP](https://www.gnupg.org/gph/en/manual.html) but it was the first time I had to effectively use it.

The message was empty with just a `msg.asc` file in it:

```
$ head msg.asc 
-----BEGIN PGP MESSAGE-----
Version: GnuPG v1

hQEMA5Rm9tOuXUEGAQgAlcrBh++K7tBf6UhLPR3MM1S3N94xfSRamHWLXMBj5dp6
9fg+a2GuQDRnta+QRgmlkgXha/6vU9eFzqx9Fh7neeFOC2aOc+8wq7KSNXjUaX0o
wRdm1Jbh7fKy9ygNKGcTkikrpuVtYj1GrLjKD5CJ0gdGvv9vQIr8bUuVE+WwKgOr
hIv4sWDXChiWahDtY8A/LktfAWd0eVZ47FzQQ/LKo89v8POxvqPACmyzDRNKkNhy
AJSu2kjA44k/f79n880lMKZ89GMYjzKISxkxWYi4ccZPOmXgYFIrx5SFDhJNPhaw
1gd3InrLpBdTYGuJZxwRcZ1SpY4v5siDLoXQHnuHONLtAZh02Viq/F0cwWuRyMk5
km2lb3OREW2bHEzHTL5U4/Vb71cup0U7js7J7WvxOR7TCzizShX4w+uRAbfuLmH+
```

So I basically knew this had been encrypted using PGP with [my public PGP key](http://keyserver.ubuntu.com/pks/lookup?op=vindex&search=bertails&fingerprint=on). I already had one because I need to [sign artifacts when publishing on Sonatype](http://www.scala-sbt.org/release/docs/Using-Sonatype.html#First+-+PGP+Signatures).

First, I install the GPG toolkit for Ubuntu:

```
$ sudo apt-get install pgpgpg
```

Then I get the sender's public key from his website and add it to my keyring ([source](http://www.math.utah.edu/~beebe/PGP-notes.html)):

```
$ pgp -ka send.pubkey
```

And I can finally extract the content.

```
$ pgp msg.asc
```

The resulting file `msg` is a typical email attachment:

```
Content-Type: multipart/mixed; boundary="a8Wt8u1KmwUX3Y2C"
Content-Disposition: inline
Content-Transfer-Encoding: 8bit


--a8Wt8u1KmwUX3Y2C
Content-Type: text/plain; charset=iso-8859-1
Content-Disposition: inline
Content-Transfer-Encoding: 8bit

...

--a8Wt8u1KmwUX3Y2C
Content-Type: application/pdf
Content-Disposition: attachment; filename="the-file.pdf"
Content-Transfer-Encoding: base64

...

--a8Wt8u1KmwUX3Y2C--
```

I still need to extract the PDF. For that, I used `munpack`:

```
$ sudo apt-get install mpack
$ munpack msg
the-file.pdf (application/pdf)
```

Et voilà!

Bonus
-----

If you have forgotten your passphrase to unlock your PGP key, you can use this command [found on stackoverflow](http://stackoverflow.com/a/11484411):

```
$ echo "1234" | gpg --no-use-agent -o /dev/null --local-user 'Alexandre Bertails <alexandre@bertails.org>' --no-greeting -as - && echo "The correct passphrase was entered for this key"
```

You can also use the `--passphrase` parameter if needed.