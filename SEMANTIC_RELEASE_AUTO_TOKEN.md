# Automatic GitHub Token Detection for semantic-release

## Overview

This project uses the **semantic-release skill's 1Password integration** (`~/.claude/skills/semantic-release/`) for automatic GitHub token selection based on directory path.

The system combines:
- **Git conditional includes** (directory-based config selection)
- **1Password CLI** (secure token retrieval)
- **Skill SSoT script** (`release_with_1password.sh`)

See: `~/.claude/skills/semantic-release/references/authentication.md` (Priority 3)

## Directory → Account Mapping

| Directory Pattern | GitHub Account | Git Config File | 1Password Item |
|-------------------|----------------|-----------------|----------------|
| `/Users/terryli/own/` | `tainora` | `~/.gitconfig-tainora` | GitHub Tainora Semantic-Release |
| `/Users/terryli/scripts/` | `tainora` | `~/.gitconfig-tainora` | GitHub Tainora Semantic-Release |
| `/Users/terryli/eon/` | `terrylica` | `~/.gitconfig-terrylica` | GitHub Terrylica Semantic-Release |

## How It Works

### 1. Git Conditional Includes (`~/.gitconfig`)

The global git config uses `includeIf` directives to load directory-specific configurations:

```gitconfig
[includeIf "gitdir:/Users/terryli/own/"]
    path = /Users/terryli/.gitconfig-tainora

[includeIf "gitdir:/Users/terryli/eon/"]
    path = /Users/terryli/.gitconfig-terrylica

[includeIf "gitdir:/Users/terryli/scripts/"]
    path = /Users/terryli/.gitconfig-tainora
```

### 2. Directory-Specific Git Config

Each included config file stores the 1Password item ID and vault ID:

**`~/.gitconfig-tainora`** (for `/own/` and `/scripts/`):
```gitconfig
[user]
    name  = tainora
    email = usalchemist@gmail.com
    githubToken1PasswordID = 7s4vhhz7e5da7x76myzn7t6wqy
    githubToken1PasswordVault = j6lqn6aeiwdvzh73z5okqpywly

[credential]
    username = tainora
```

**`~/.gitconfig-terrylica`** (for `/eon/`):
```gitconfig
[user]
    githubToken1PasswordID = 53evlbkz3udnykztzir77wg7ku
    githubToken1PasswordVault = j6lqn6aeiwdvzh73z5okqpywly

[credential]
    username = terrylica
```

### 3. Skill Script (`~/.claude/skills/semantic-release/scripts/release_with_1password.sh`)

The universal skill script:
1. Reads `user.githubToken1PasswordID` and `user.githubToken1PasswordVault` from git config
2. Retrieves the GitHub token from 1Password using `op item get --reveal`
3. Exports `GITHUB_TOKEN` environment variable
4. Runs `npx semantic-release` with the correct token

**SSoT**: Script lives in semantic-release skill, not duplicated per-project

## Usage

### Automatic Token Selection (Recommended)

```bash
npm run release:auto
```

This automatically:
- Detects the current directory
- Loads the appropriate git config via conditional includes
- Retrieves the correct GitHub token from 1Password
- Runs semantic-release in production mode (`CI=true`)

### Manual Token (Not Recommended)

```bash
GITHUB_TOKEN=$(op item get <item-id> --vault <vault-id> --fields label=token) npm run release
```

### Dry Run (Test Without Creating Release)

```bash
npm run release:dry
```

## Verification

Check which token will be used in the current directory:

```bash
# Check which git user identity is active
git config --get user.name
git config --get user.email

# Check which 1Password item will be used
git config --get user.githubToken1PasswordID
git config --get user.githubToken1PasswordVault
```

**Example in `/Users/terryli/own/netstrata`**:
```bash
$ git config --get user.name
tainora

$ git config --get user.githubToken1PasswordID
7s4vhhz7e5da7x76myzn7t6wqy
```

**Example in `/Users/terryli/eon/some-project`**:
```bash
$ git config --get user.name
terrylica

$ git config --get user.githubToken1PasswordID
53evlbkz3udnykztzir77wg7ku
```

## Adding New Directory Mappings

To add a new directory pattern:

1. **Add conditional include to `~/.gitconfig`**:
   ```gitconfig
   [includeIf "gitdir:/Users/terryli/new-directory/"]
       path = /Users/terryli/.gitconfig-<account>
   ```

2. **Create or update the account-specific config**:
   ```gitconfig
   [user]
       name = <github-username>
       email = <email>
       githubToken1PasswordID = <1password-item-id>
       githubToken1PasswordVault = <1password-vault-id>

   [credential]
       username = <github-username>
   ```

3. **Test the configuration**:
   ```bash
   cd /Users/terryli/new-directory/some-repo
   git config --get user.name  # Should show the expected username
   git config --get user.githubToken1PasswordID  # Should show the 1Password item ID
   ```

## Troubleshooting

### Error: "Git config missing GitHub token 1Password credentials"

**Cause**: The current directory is not matched by any conditional include, or the matched config file doesn't have the required values.

**Solution**:
1. Check current directory: `pwd`
2. Check which git config is loaded: `git config --get user.name`
3. Verify conditional includes in `~/.gitconfig`
4. Verify the included config file has `user.githubToken1PasswordID` and `user.githubToken1PasswordVault`

### Error: "Failed to retrieve token from 1Password"

**Cause**: 1Password CLI (`op`) is not authenticated, or the item ID/vault ID is incorrect.

**Solution**:
1. Authenticate with 1Password CLI: `op signin`
2. Verify item exists: `op item get <item-id> --vault <vault-id>`
3. Check the item has a field labeled "token"

## Benefits

✅ **Zero manual token management**: Never pass `GITHUB_TOKEN=` manually
✅ **Automatic account detection**: Switch directories, tokens switch automatically
✅ **Secure**: Tokens stored in 1Password, never in git repos or shell history
✅ **Consistent with SSH**: Same directory-based routing as SSH config
✅ **Auditable**: `git config` commands show exactly which account/token is active

## References

- [Git Conditional Includes Documentation](https://git-scm.com/docs/git-config#_conditional_includes)
- [semantic-release CI Configuration](https://semantic-release.gitbook.io/semantic-release/usage/ci-configuration)
- [1Password CLI Documentation](https://developer.1password.com/docs/cli/)
