const originalSlides = [
  {
    "title": "What is Caching?",
    "content": "### Definition:\nCaching is a technique where you store a copy of data in a temporary storage location (cache) so that future requests for that data are faster. Instead of re-computing or re-fetching, you reuse the previously fetched or computed data.",
    "slide_type": "text"
  },
  {
    "title": "Why Use Caching?",
    "content": "### Benefits:\n- 🚀 Reduces latency\n- 📉 Reduces backend load\n- 📈 Improves scalability\n- 😀 Enhances user experience\n\nCaching helps applications respond faster and handle more load efficiently.",
    "slide_type": "text"
  },
  {
    "title": "Caching Analogy",
    "content": "### Real-World Analogy:\nIf you frequently need a book in a library, keeping a copy at your desk avoids walking to the shelf repeatedly. Caching does the same for data.",
    "slide_type": "text"
  },
  {
    "title": "Types of Caches",
    "content": "### Common Types:\n- **In-memory cache** (e.g., Redis, Memcached)\n- **Disk cache** (e.g., browser storage)\n- **Browser cache** (e.g., static files, scripts)\n- **CDN cache** (e.g., Cloudflare, Akamai)\n- **Application cache** (function outputs or service responses)",
    "slide_type": "text"
  },
  {
    "title": "Where Caching Can Be Applied",
    "content": "### Common Use Cases:\n- 🖥️ Web applications: cache HTML, API responses\n- 🔙 Backend services: cache computations, service responses\n- 🧮 Databases: cache queries, use materialized views\n- 📲 Mobile apps: cache offline API data",
    "slide_type": "text"
  },
  {
    "title": "Caching Strategies",
    "content": "### Key Strategies:\n- **Read-through**: Get from cache → If miss → Fetch + store\n- **Write-through**: Write to both cache and DB\n- **Write-behind**: Write to cache first, DB updated later\n- **Cache Invalidation**: TTL, event-based, or manual",
    "slide_type": "text"
  },
  {
    "title": "Cache Invalidation",
    "content": "### How to Keep Cache Fresh:\n- **TTL (Time To Live)**: Auto-expiry after duration\n- **Manual Invalidation**: When data is updated or deleted\n- **Event-Driven**: Update cache when system events occur",
    "slide_type": "text"
  },
  {
    "title": "When Not to Use Caching",
    "content": "### Avoid Caching When:\n- Data changes frequently (high volatility)\n- Strong consistency is required\n- Sensitive or user-specific data (unless user-level caching is used)",
    "slide_type": "text"
  },
  {
    "title": "Cache Eviction Policies",
    "content": "### How Cache Decides What to Remove:\n- **LRU**: Least Recently Used\n- **LFU**: Least Frequently Used\n- **FIFO**: First In First Out\n- **Random**: Removes a random entry",
    "slide_type": "text"
  },
  {
    "title": "Multi-layered Cache System",
    "content": "### Typical Layers:\n```\n[User Request]\n     ↓\n[Browser Cache]\n     ↓\n[CDN Cache]\n     ↓\n[Application Cache]\n     ↓\n[Database]\n```\nEach layer reduces load and latency for the next.",
    "slide_type": "code"
  },
  {
    "title": "Risks and Challenges in Caching",
    "content": "### Common Pitfalls:\n- ⚠️ Stale Data: Users may see outdated info\n- ⚠️ Cache Stampede: High load on cache miss\n- ⚠️ Memory Overhead: Large data volumes\n- ⚠️ Security: Caching sensitive data can be risky",
    "slide_type": "text"
  },
  {
    "title": "Best Practices for Caching",
    "content": "### Tips for Effective Caching:\n- Set appropriate TTL values\n- Use meaningful cache keys\n- Monitor cache hit/miss ratio\n- Implement fallback mechanism when cache is down",
    "slide_type": "text"
  },
  {
    "title": "Real-world Examples of Caching",
    "slide_type": "table",
    "content": [
      {"Use Case": "Product list page", "Cache Used": "Redis"},
      {"Use Case": "Search autocomplete", "Cache Used": "In-memory cache"},
      {"Use Case": "User sessions", "Cache Used": "JWT or Redis"},
      {"Use Case": "Image delivery", "Cache Used": "CDN"},
      {"Use Case": "Weather API", "Cache Used": "Location-based cache"}
    ]
  },
  {
    "title": "Memoization Example in Python",
    "content": "### Code Snippet:\n```python\ndef fib(n, cache={}):\n    if n in cache:\n        return cache[n]\n    if n <= 1:\n        return n\n    cache[n] = fib(n-1, cache) + fib(n-2, cache)\n    return cache[n]\n```",
    "slide_type": "code"
  },
  {
    "title": "Redis Caching Example in Node.js",
    "content": "### Code Snippet:\n```javascript\nconst redis = require('redis');\nconst client = redis.createClient();\n\napp.get('/data', async (req, res) => {\n  const cached = await client.get('data-key');\n  if (cached) return res.send(JSON.parse(cached));\n  const data = await fetchDataFromDB();\n  client.setex('data-key', 3600, JSON.stringify(data));\n  res.send(data);\n});\n```",
    "slide_type": "code"
  }
];  // paste first JSON here
const updatedSlides = [
  {
    "title": "What is Caching?",
    "content": "### Definition:\nCaching is a data storage technique where frequently accessed or expensive-to-fetch data is stored temporarily in a high-speed storage layer. This allows subsequent requests for the same data to be served faster.\n\n### Depth:\nCaching works by temporarily storing copies of data in a high-speed layer like RAM. This avoids frequent round-trips to slower data sources like databases or APIs. The cache can be local (on the same server), distributed (shared across servers), or layered (multiple cache levels). Modern applications often use caching to meet performance SLAs and reduce infrastructure costs.",
    "slide_type": "text"
  },
  {
    "title": "Why Use Caching?",
    "content": "### Benefits:\n- 🚀 **Reduces latency**: By storing results closer to the user or computation layer, data retrieval is much faster.\n- 📉 **Reduces backend load**: Caching offloads repetitive processing from databases and APIs.\n- 📈 **Improves scalability**: Applications can handle more traffic with the same resources.\n- 😀 **Enhances user experience**: Faster response times mean better usability and customer satisfaction.\n\n### Depth:\nCaching significantly improves the efficiency of system resources. For example, instead of querying a database 10,000 times for the same product details, a single query result can be cached and reused. This not only speeds up delivery but also protects the database from heavy read loads.",
    "slide_type": "text"
  },
  {
    "title": "Caching Analogy",
    "content": "### Real-World Analogy:\nImagine a student often refers to the same formula in a textbook. Instead of flipping through pages every time, they write it on a sticky note placed nearby. Similarly, caching keeps frequently used data within easy reach, reducing effort and time to access it.\n\n### Depth:\nThis analogy mirrors how in-memory caches operate. Rather than always fetching data from a remote server or disk, systems keep frequently accessed information close by, just like the student’s sticky note for quicker reference.",
    "slide_type": "text"
  },
  {
    "title": "Types of Caches",
    "content": "### Common Types:\n- **In-memory cache** (e.g., Redis, Memcached): High-speed storage in RAM, best for fast access.\n- **Disk cache**: Stores data on disk, useful for large data sets that don't fit in RAM.\n- **Browser cache**: Local storage used by browsers to store static files like CSS, JS, and images.\n- **CDN cache**: Global servers store copies of content closer to users.\n- **Application cache**: Caching at code or business logic level (e.g., function outputs, computed values).\n\n### Depth:\nEach type of cache serves a different layer of the technology stack. For example, browser and CDN caches optimize content delivery at the network level, while in-memory caches like Redis speed up server-side computations or API responses. Selecting the right cache type depends on latency tolerance, data volume, and update frequency.",
    "slide_type": "text"
  },
  {
    "title": "Where Caching Can Be Applied",
    "content": "### Common Use Cases:\n- 🖥️ **Web applications**: Cache HTML pages or frequently used API responses to reduce server load.\n- 🔙 **Backend services**: Cache expensive operations like aggregations or third-party API calls.\n- 🧮 **Databases**: Use query result caching, in-memory views, or replicas to offload read-heavy operations.\n- 📲 **Mobile apps**: Store static or semi-static data locally to reduce network usage and improve performance.\n\n### Depth:\nCaching can be integrated at multiple architectural points—from front-end browsers to backend data services. For example, a frequently accessed product list in an e-commerce app can be cached at the API layer to prevent redundant database hits, while real-time stock prices may need selective caching with shorter TTLs.",
    "slide_type": "text"
  },
  {
    "title": "Caching Strategies",
    "content": "### Key Strategies:\n- **Read-through**: Application queries the cache; if data isn’t present, it fetches from the source and updates the cache.\n- **Write-through**: Data is written to the cache and backend store simultaneously.\n- **Write-behind (Write-back)**: Writes go to cache first and are persisted to the backend asynchronously.\n- **Cache Invalidation**: Ensures cache doesn’t serve outdated data using TTLs, manual controls, or event-driven updates.\n\n### Depth:\nEach strategy suits different consistency and latency requirements. For example, write-behind can improve write performance but may risk data loss on crash. Choosing the right strategy involves understanding system load, data consistency needs, and failure tolerance.",
    "slide_type": "text"
  },
  {
    "title": "Cache Invalidation",
    "content": "### How to Keep Cache Fresh:\n- **TTL (Time To Live)**: Automatically expires entries after a specified duration.\n- **Manual Invalidation**: Explicitly remove or refresh cache entries when data changes.\n- **Event-Driven**: Use system events to trigger cache refresh or invalidation (e.g., after a DB update).\n\nProper invalidation is essential to avoid serving stale or incorrect data.\n\n### Depth:\nInvalidation is often the hardest part of caching. A poorly invalidated cache can lead to data inconsistencies. Systems may combine TTLs with publish-subscribe patterns to manage invalidation efficiently, especially in distributed architectures.",
    "slide_type": "text"
  },
  {
    "title": "When Not to Use Caching",
    "content": "### Avoid Caching When:\n- **High data volatility**: Caching can lead to inconsistencies if data changes rapidly.\n- **Strong consistency requirements**: Applications that demand up-to-the-millisecond accuracy may suffer.\n- **Sensitive or dynamic data**: User-specific data like payment info should be handled cautiously or excluded from caching.\n\n### Depth:\nIn such cases, caching may do more harm than good. For example, banking transactions require strong ACID properties and real-time accuracy, which caching can compromise. Always evaluate consistency and data freshness needs before implementing caching.",
    "slide_type": "text"
  },
  {
    "title": "Cache Eviction Policies",
    "content": "### How Cache Decides What to Remove:\n- **LRU (Least Recently Used)**: Removes data not accessed for the longest time.\n- **LFU (Least Frequently Used)**: Evicts data with the fewest accesses.\n- **FIFO (First In First Out)**: Removes the oldest stored data.\n- **Random**: Deletes a random entry.\n\nChoosing the right policy ensures memory efficiency and optimal cache performance.\n\n### Depth:\nEviction policies help maintain cache size limits. For example, LRU is commonly used in systems where recent access patterns predict future use. In contrast, LFU is better when frequently accessed items should persist longer. Some systems use hybrid policies to balance access recency and frequency.",
    "slide_type": "text"
  },
  {
    "title": "Risks and Challenges in Caching",
    "content": "### Common Pitfalls:\n- ⚠️ **Stale Data**: Without proper invalidation, users may receive outdated information.\n- ⚠️ **Cache Stampede**: If many requests trigger the same cache miss, it can overload backend systems.\n- ⚠️ **Memory Overhead**: Caching large volumes of data may consume excessive RAM or storage.\n- ⚠️ **Security Issues**: Storing sensitive or personal data in cache without protection can lead to leaks.\n\n### Depth:\nTo mitigate these issues, engineers use patterns like mutex locks or request coalescing to prevent stampedes, set memory usage limits, and apply encryption for sensitive cache entries.",
    "slide_type": "text"
  },
  {
    "title": "Best Practices for Caching",
    "content": "### Tips for Effective Caching:\n- Set appropriate TTLs to ensure freshness\n- Use unique and scoped cache keys to prevent collisions\n- Monitor cache hit/miss ratios for optimization\n- Implement graceful fallback when cache fails\n- Separate concerns: don’t cache everything blindly; know what to cache and why\n\n### Depth:\nFollowing best practices can ensure caching works in your favor. For example, monitoring hit/miss ratios reveals inefficiencies. Also, fallback mechanisms ensure applications don’t crash or delay too much in case of a cache outage.",
    "slide_type": "text"
  }
];   // paste second JSON here

// Create a lookup map from the second JSON for quick access
const updatedMap = new Map();
updatedSlides.forEach(slide => {
  updatedMap.set(slide.title, slide);
});

const finalSlides = originalSlides.map(slide => {
  if (updatedMap.has(slide.title)) {
    const updated = updatedMap.get(slide.title);
    return {
      ...slide,
      content: updated.content,
      slide_type: updated.slide_type
    };
  }
  return slide; // keep original if no update found
});

console.log(JSON.stringify(finalSlides, null, 2));
