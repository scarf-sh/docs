# Making Sense of Your Scarf Insights

Your Scarf dashboard uses various technical terms that are important to understand.

### Unique Sources

Scarf denotes how many `sources` or `unique sources` were behind any given number of events. Because open source activity happens anonymously, Scarf's ability to form a stable anonymous ID for a given user / source of traffic can happen at multiple levels of granularity, and therefor are given different types of IDs.

#### Origin IDs

An `origin_id` is the most granular of Scarf IDs, and the default notion of unique sources throughout the platform.

An `origin_id` is a salted hash of every identifier available to Scarf in an HTTP request: the IP address, the user agent, and any other identifying headers that might be available.

An individual developer may map to multiple `origin_ids` as they change IP addresses, or use different programs on their machine to make requests. Thus it is good to consider it a ceiling or slightly higher estimate of how many people are behind the activity you are tracking.

This makes `origin_id`s a useful way to approximate individual developer activity, but they are not a perfect one-to-one mapping to people. Instead, you can think of them as the most fine-grained view Scarf provides. They are helpful for estimating upper bounds on unique developers/deployments.

#### Endpoint IDs

An `endpoint_id` is the least granular Scarf source ID, which is a salted hash of just the IP address. Unlike `origin_id`s, which consider multiple request attributes, `endpoint_id`s group together all activity that appears to come from the same network location.

Because many developers in an organization might share the same IP (for example, when working behind a corporate NAT or build server), multiple people / machines can collapse into a single endpoint_id. Conversely, a single individual may generate multiple `endpoint_id`s if they work from different networks, such as switching between home, office, and cloud environments.

This makes `endpoint_id`s a good way to reason about unique network sources, but they are not a direct proxy for individual people. Instead, you can think of them as a middle ground: less noisy than `origin_id`s but still more fine-grained than company-level resolution.

