#!/usr/bin/env python
# coding: utf-8

# In[2]:


#UK Corporate Contact & Regional Directory Dataset


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


df = pd.read_csv(r"C:\Users\Samson\Downloads\UK_Corporate_Contact_&_Regional_Directory_Dataset.csv")
df


# In[11]:


sns.set_theme(style="whitegrid")


# In[12]:


#Regional Business Concentration (Top Counties)
#Identifies the primary geographic hubs by counting records per county.


# In[14]:


plt.figure(figsize=(8, 4))
top_counties = df['county'].value_counts().head(5)


# In[16]:


sns.barplot(
    x=top_counties.values, 
    y=top_counties.index, 
    hue=top_counties.index, 
    palette='Blues_r', 
    legend=False
)
plt.title('Top 5 UK Counties by Business Count', fontsize=12, fontweight='bold')
plt.xlabel('Number of Companies')
plt.ylabel('County')
plt.tight_layout()
plt.show()


# In[18]:


#Key Takeaway: Greater London and Greater Manchester represent over 13% of all registered listings.

total_listings = len(df)
combined_count = df['county'].isin(['Greater London', 'Greater Manchester']).sum()
percentage = (combined_count / total_listings) * 100


# In[19]:


print(f"Greater London & Manchester Total: {combined_count}")
print(f"Total Dataset Listings: {total_listings}")
print(f"Combined Market Share: {percentage:.2f}%")


# In[21]:


#Email Provider Classification (Public vs. Corporate)


# In[22]:


plt.figure(figsize=(6, 6))
df['email_domain'] = df['email'].apply(lambda x: x.split('@')[1])
df['email_type'] = df['email_domain'].apply(lambda d: 'Public Webmail' if d in ['gmail.com', 'yahoo.com', 'hotmail.com'] else 'Custom Domain')


# In[25]:


counts = df['email_type'].value_counts()
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, 
        colors=['#4c72b0', '#55a868'], wedgeprops=dict(width=0.4, edgecolor='w'))

plt.title('Email Provider Type Distribution', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('insight_2_email_types.png', dpi=300)
plt.show()


# In[26]:


df['email_domain'] = df['email'].apply(lambda x: x.split('@')[1])

public_domains = ['gmail.com', 'yahoo.com', 'hotmail.com']
df['email_type'] = df['email_domain'].apply(
    lambda d: 'Public Webmail' if d in public_domains else 'Custom Corporate Domain'
)

counts = df['email_type'].value_counts()
percentages = df['email_type'].value_counts(normalize=True) * 100


# In[27]:


for category in counts.index:
    print(f"{category}: {counts[category]} ({percentages[category]:.1f}%)")


# In[28]:


#Postcode Area Prefix Mapping (Vertical Bar Chart)


# In[29]:


plt.figure(figsize=(8, 4))
df['postcode_prefix'] = df['postal'].str.extract(r'^([A-Z]{1,2})', expand=False)
top_postcodes = df['postcode_prefix'].value_counts().head(5)


# In[30]:


sns.barplot(x=top_postcodes.index, y=top_postcodes.values, palette='crest')
plt.title('Top 5 Postal Area Prefixes', fontsize=12, fontweight='bold')
plt.xlabel('Postcode Prefix')
plt.ylabel('Company Count')
plt.tight_layout()
plt.savefig('insight_3_postcode_prefixes.png', dpi=300)
plt.show()


# In[31]:


df['postcode_prefix'] = df['postal'].str.extract(r'^([A-Z]{1,2})', expand=False)

city_map = {
    'B': 'Birmingham',
    'NE': 'Newcastle',
    'S': 'Sheffield',
    'BN': 'Brighton',
    'NG': 'Nottingham'
}

top_prefixes = df['postcode_prefix'].value_counts().head(5)


# In[32]:


for prefix, count in top_prefixes.items():
    city_name = city_map.get(prefix, 'Other')
    print(f"{prefix} ({city_name}): {count}")


# In[34]:


#Street Address Naming Conventions (Horizontal Bar Chart)


# In[35]:


plt.figure(figsize=(8, 4))
df['street_suffix'] = df['address'].str.extract(r'\b(St|Rd|Street|Road|Ave|Lane|Place)\b', expand=False)
suffix_counts = df['street_suffix'].value_counts()


# In[36]:


sns.barplot(x=suffix_counts.values, y=suffix_counts.index, palette='viridis')
plt.title('Street Address Type Frequency', fontsize=12, fontweight='bold')
plt.xlabel('Count')
plt.ylabel('Street Suffix')
plt.tight_layout()
plt.savefig('insight_4_street_types.png', dpi=300)
plt.show()


# In[38]:


df['street_suffix'] = df['address'].str.extract(r'\b(St|Rd|Place|Lane)\b', expand=False)


# In[58]:


suffix_counts = df['street_suffix'].value_counts()

suffix_map = {
    'St': 'St (Street)',
    'Rd': 'Rd (Road)',
    'Place': 'Place',
    'Lane': 'Lane'
}


# In[59]:


for key, label in suffix_map.items():
    count = suffix_counts.get(key, 0)
    print(f"{label}: {count}")


# In[60]:


#Local Administrative Ward Density (Horizontal Bar Chart)


# In[61]:


plt.figure(figsize=(8, 4))
top_cities = df['city'].value_counts().head(5)


# In[62]:


sns.barplot(x=top_cities.values, y=top_cities.index, palette='mako')
plt.title('Top Administrative Cities / Wards by Listings', fontsize=12, fontweight='bold')
plt.xlabel('Count')
plt.ylabel('City / Ward')
plt.tight_layout()
plt.savefig('insight_9_ward_density.png', dpi=300)
plt.show()


# In[63]:


top_cities = df['city'].value_counts().head(4)


# In[64]:


for city, count in top_cities.items():
    print(f"{city}: {count}")


# In[68]:


#Founder-Named Business Detection (Donut Chart)


# In[69]:


plt.figure(figsize=(6, 6))
df['is_founder_named'] = df.apply(lambda r: r['last_name'].lower() in r['company_name'].lower(), axis=1)
founder_counts = df['is_founder_named'].map({True: 'Surname Included', False: 'Independent Name'}).value_counts()


# In[70]:


plt.pie(founder_counts, labels=founder_counts.index, autopct='%1.1f%%', 
        colors=['#e74c3c', '#3498db'], wedgeprops=dict(width=0.4, edgecolor='w'))
plt.title('Founder Surname Inclusion in Company Name', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('insight_7_founder_names.png', dpi=300)


# In[71]:


df['has_surname'] = df.apply(
    lambda row: str(row['last_name']).lower() in str(row['company_name']).lower(), 
    axis=1
)

false_count = (df['has_surname'] == False).sum()
true_count = (df['has_surname'] == True).sum()
overlap_pct = (true_count / len(df)) * 100


# In[72]:


print(f"False: {false_count} ({overlap_pct:.0f}% overlap between personal surnames and trade names)")


# In[73]:


#Telephone Area Code (STD) Frequency (Bar Chart)


# In[74]:


plt.figure(figsize=(8, 4))
df['std_code'] = df['phone1'].str.split('-').str[0]
top_std = df['std_code'].value_counts().head(5)


# In[75]:


sns.barplot(x=top_std.index, y=top_std.values, palette='magma')
plt.title('Top 5 Primary Telephone STD Codes', fontsize=12, fontweight='bold')
plt.xlabel('STD Code')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('insight_5_std_codes.png', dpi=300)
plt.show()


# In[77]:


df['std_code'] = df['phone1'].str.split('-').str[0]

std_map = {
    '01567': 'Killin',
    '01270': 'Crewe',
    '01536': 'Kettering'
}

top_std = df['std_code'].value_counts().head(3)


# In[78]:


for code, count in top_std.items():
    town_name = std_map.get(code, 'Other')
    print(f"{code} ({town_name}): {count}")


# In[ ]:




