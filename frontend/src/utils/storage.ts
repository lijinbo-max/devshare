export const getStorageItem = <T>(key: string, defaultValue: T): T => {
  try {
    const item = localStorage.getItem(key)
    return item ? JSON.parse(item) : defaultValue
  } catch {
    return defaultValue
  }
}

export const setStorageItem = <T>(key: string, value: T): void => {
  try {
    localStorage.setItem(key, JSON.stringify(value))
  } catch (error) {
    console.error('Failed to set storage item:', error)
  }
}

export const removeStorageItem = (key: string): void => {
  try {
    localStorage.removeItem(key)
  } catch (error) {
    console.error('Failed to remove storage item:', error)
  }
}

export const clearStorage = (): void => {
  try {
    localStorage.clear()
  } catch (error) {
    console.error('Failed to clear storage:', error)
  }
}

export const StorageKeys = {
  THEME: 'theme',
  USER_PREFERENCES: 'user_preferences',
  VIEWED_POSTS: 'viewed_posts'
} as const
