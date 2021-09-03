# NameGen
Hosts a website for a modern (website/app/project/website/anything...) name generator

# API
Yes, *NameGen* comes with an extremely easy to use API :)

No JSON, no auth, no token, no anything. Just a **raw response** you'd expect.

### Without domain checking
Just generate a name, don't check any domain availability.

**URL path:**
```html
/raw
```
**Example response:**
```
Zenulas
```

### With domain checking
Generate a name and then check it's domain availability using a specific TLD (top  level domain), e.g. `.com` or `.net`.

**URL syntax:**
```html
/raw?tld=<tld_to_check>
```

> **Warning:** Don't use a dot (`.`) in the parameter, see the example below.
> 
**Example syntax:**
```html
/raw?tld=com
```

**Example response:**
```
TurboOne ✔
```

The check mark emoji (`✔`) indicates, that the domain is **available**. Keep in mind that there's a space before the emoji.

# Technologies used
## Backend
- Flask
## Frontend
- BootstrapMade (https://bootstrapmade.com/resi-free-bootstrap-html-template/download/)

# Credits
Thanks to BootstrapMade for the beautiful design!
Inspiration/Ideas:
- https://namelix.com/
- https://www.followchain.org/cool-usernames/
- https://coolestwords.com/cool-usernames/