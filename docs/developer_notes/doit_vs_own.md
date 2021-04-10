# Doit vs own framework

A large portion of Doit is targeted at providing the CLI interface,
and it is actually a much smaller part of the codebase that is geared
towards what Archimedes needs: A dependency graph framework.

We could adopt the approach of Nikola and do a moderate amount of
'patching' on Doit to make it fit our needs.

Alternatively we could use Typer for the CLI interface and use our own
dependency solver behind the scenes.

---

> Jeppe Klitgaard, 2021-04-10
